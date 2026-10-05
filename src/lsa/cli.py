"""Command-line entry point: `uv run lsa <command>`."""

from __future__ import annotations

import argparse
import csv
import json
import logging
from dataclasses import asdict
from datetime import UTC, datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import ClassVar

from lsa import paths

log = logging.getLogger(__name__)

WORDS_TO_TOKENS = 1.33


def _stamp() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def _load_queries(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _count_hn(args: argparse.Namespace) -> list:
    from lsa import count as cnt

    if not args.terms.exists():
        raise SystemExit(f"terms csv not found: {args.terms}")
    from lsa.sources import hn

    snapshot = args.snapshot or hn.snapshot_path()
    if not snapshot.exists():
        raise SystemExit(f"snapshot not found: {snapshot}")
    terms = cnt.load_terms(args.terms)
    if args.limit:
        terms = terms[: args.limit]
    return hn.count_terms(snapshot, terms)


def _planned(source, family, region, category, system, query, stamp):
    from lsa.contracts import CountRecord

    return CountRecord(
        source=source,
        family=family,
        region=region,
        category=category,
        system=system,
        query=query,
        count=None,
        method="dry-run",
        counted_at=stamp,
    )


def _count_jobs_pages(args: argparse.Namespace, client=None) -> list:
    from lsa.sources import jobpages

    rows = _load_queries(args.queries)
    if args.limit:
        rows = rows[: args.limit]
    stamp = _stamp()
    records = []
    for row in rows:
        if client is None:
            records.extend(
                _planned(
                    site.key,
                    "jobs-pages",
                    row["region"],
                    row["category"],
                    "",
                    row["query"],
                    stamp,
                )
                for site in jobpages.SITES_BY_REGION.get(row["region"], ())
            )
            continue
        try:
            records.extend(
                jobpages.records_for_query(
                    row["query"],
                    row["region"],
                    row["category"],
                    client,
                    stamp,
                )
            )
        except Exception as exc:  # noqa: BLE001 - log and skip per source
            log.warning("jobs-pages %s/%s: %s", row["region"], row["query"], exc)
    return records


def _count_vendor(args: argparse.Namespace, client=None) -> list:
    from lsa.sources import sitemaps

    sites = sitemaps.load_sites(args.sites)
    if args.limit:
        sites = sites[: args.limit]
    stamp = _stamp()
    records = []
    for site in sites:
        if client is None:
            records.extend(
                _planned(
                    site.domain,
                    site.family,
                    "US",
                    category,
                    site.vendor,
                    site.story_path_regex,
                    stamp,
                )
                for category in site.categories or ("",)
            )
            continue
        try:
            records.extend(sitemaps.records_for_site(site, client, stamp))
        except Exception as exc:  # noqa: BLE001 - log and skip per source
            log.warning("vendor %s: %s", site.domain, exc)
    return records


def _count_reddit(args: argparse.Namespace, client=None) -> list:
    from lsa.sources import reddit

    rows = _load_queries(args.queries)
    if args.limit:
        rows = rows[: args.limit]
    stamp = _stamp()
    records = []
    for row in rows:
        if client is None:
            records.append(
                _planned(
                    "reddit",
                    "reddit",
                    row["region"],
                    row["category"],
                    "",
                    row["query"],
                    stamp,
                )
            )
            continue
        try:
            records.append(
                reddit.record_for_query(
                    row["query"],
                    row["region"],
                    row["category"],
                    client,
                    stamp,
                )
            )
        except Exception as exc:  # noqa: BLE001 - log and skip per source
            log.warning("reddit %s/%s: %s", row["region"], row["query"], exc)
    return records


def _count_pages_family(counter, args: argparse.Namespace) -> list:
    if args.dry_run:
        return counter(args)
    from lsa.sources import http

    with http.make_client() as client:
        return counter(args, client)


_COUNTERS = {
    "hn": _count_hn,
    "jobs-pages": _count_jobs_pages,
    "vendor": _count_vendor,
    "reddit": _count_reddit,
}


def _count(args: argparse.Namespace) -> None:
    from lsa import count as cnt

    counter = _COUNTERS.get(args.family)
    if counter is None:
        raise SystemExit(
            f"family {args.family!r} unknown "
            f"(implemented: {', '.join(sorted(_COUNTERS))})"
        )
    if args.family == "hn":
        records = counter(args)
    else:
        records = _count_pages_family(counter, args)
    print(cnt.format_table(records))
    if args.dry_run:
        print(f"dry run: {len(records)} rows, nothing written")
        return
    out = cnt.append_counts(records, args.counts)
    print(f"wrote {len(records)} rows to {out}")
    if args.family == "hn":
        from lsa.sources import hn

        snapshot = args.snapshot or hn.snapshot_path()
        terms = cnt.load_terms(args.terms)
        proxy = hn.sample_token_lengths(snapshot, terms)
        print(f"token proxy: {proxy:.1f} tokens/comment (word_count x 1.33)")


class _TextExtractor(HTMLParser):
    """Collects visible text; script/style/head content is dropped."""

    _SKIP: ClassVar[set[str]] = {
        "script", "style", "head", "noscript", "template"
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._depth = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag in self._SKIP:
            self._depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in self._SKIP and self._depth:
            self._depth -= 1

    def handle_data(self, data: str) -> None:
        if not self._depth:
            self.parts.append(data)


def _word_count(html_text: str) -> int:
    parser = _TextExtractor()
    parser.feed(html_text)
    return len(" ".join(parser.parts).split())


def _sample_page(
    url: str, client, raw_dir: Path, index: int
) -> tuple[int, Path | None]:
    """Fetch one page; returns (word_count, raw_path) or (0, None)."""
    from lsa.sources import http, robots

    if not robots.allowed(url, client):
        return 0, None
    try:
        response = http.get_with_backoff(client, url)
    except Exception as exc:  # noqa: BLE001 - a failed page just drops out
        log.warning("sample fetch %s: %s", url, exc)
        return 0, None
    if response.status_code != 200:
        log.warning("sample fetch %s -> HTTP %s", url, response.status_code)
        return 0, None
    raw_dir.mkdir(parents=True, exist_ok=True)
    raw_path = raw_dir / f"page-{index:03d}.html"
    raw_path.write_bytes(response.content)
    return _word_count(response.text), raw_path


def _candidate_urls(args: argparse.Namespace, client) -> list[str]:
    from lsa.sources import jobpages, sitemaps

    if args.family == "vendor":
        sites = sitemaps.load_sites(args.sites)
        return sitemaps.sample_story_urls(sites, client, args.n * 3)
    rows = _load_queries(args.queries)
    urls = []
    for site in jobpages.SITES:
        for row in rows:
            if row["region"] == site.region:
                urls.append(site.url(row["query"]))
            if len(urls) >= args.n * 3:
                break
        if len(urls) >= args.n * 3:
            break
    return urls


def _sample_tokens(args: argparse.Namespace) -> None:
    from lsa.sources import http

    raw_dir = paths.RAW / "sample-pages" / args.family
    counts: list[int] = []
    with http.make_client() as client:
        for url in _candidate_urls(args, client):
            if len(counts) >= args.n:
                break
            words, _ = _sample_page(url, client, raw_dir, len(counts))
            if words:
                counts.append(words)
    if not counts:
        print(f"{args.family}: no pages fetched")
        return
    mean_words = sum(counts) / len(counts)
    print(
        f"{args.family}: {len(counts)} pages, "
        f"{mean_words:.0f} mean words, "
        f"{mean_words * WORDS_TO_TOKENS:.0f} tokens/item (x{WORDS_TO_TOKENS})"
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="lsa")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_count = sub.add_parser(
        "count", help="count items per source and upsert counts.parquet"
    )
    p_count.add_argument("--family", required=True, help="count family to run")
    p_count.add_argument(
        "--terms",
        type=Path,
        default=paths.RESEARCH / "search_terms.csv",
        help="category,region,term csv of search terms",
    )
    p_count.add_argument(
        "--queries",
        type=Path,
        default=paths.RESEARCH / "count_queries.csv",
        help="category,region,query,lang csv for jobs-pages and reddit",
    )
    p_count.add_argument(
        "--sites",
        type=Path,
        default=paths.RESEARCH / "vendor_sites.csv",
        help="vendor,domain,story_path_regex,categories csv for vendor",
    )
    p_count.add_argument(
        "--counts",
        type=Path,
        default=None,
        help="counts parquet to upsert (default: data/derived/counts.parquet)",
    )
    p_count.add_argument(
        "--snapshot",
        type=Path,
        default=None,
        help="override LSA_HN_SNAPSHOT / the default HN snapshot path",
    )
    p_count.add_argument(
        "--dry-run",
        action="store_true",
        help="print planned rows without fetching or writing",
    )
    p_count.add_argument(
        "--limit",
        type=int,
        default=None,
        help="cap query rows (jobs-pages, reddit) or sites (vendor)",
    )
    p_count.set_defaults(func=_count)

    p_tokens = sub.add_parser(
        "sample-tokens",
        help="mean words x 1.33 over fetched pages for one family",
    )
    p_tokens.add_argument(
        "--family",
        required=True,
        choices=["vendor", "jobs-pages"],
        help="page family to sample",
    )
    p_tokens.add_argument("--n", type=int, default=30)
    p_tokens.add_argument(
        "--queries",
        type=Path,
        default=paths.RESEARCH / "count_queries.csv",
    )
    p_tokens.add_argument(
        "--sites",
        type=Path,
        default=paths.RESEARCH / "vendor_sites.csv",
    )
    p_tokens.set_defaults(func=_sample_tokens)

    p_est = sub.add_parser(
        "estimate", help="print a Jev cost estimate from counted items"
    )
    p_est.add_argument(
        "--counts",
        type=Path,
        default=paths.DERIVED / "counts.parquet",
        help="parquet of CountRecord rows from the collectors",
    )
    p_est.add_argument(
        "--passes",
        type=Path,
        default=paths.ROOT / "configs" / "passes.toml",
    )
    p_est.add_argument(
        "--prices",
        type=Path,
        default=paths.ROOT / "configs" / "prices.toml",
    )
    p_est.add_argument("--model", default="jev-1.13.0")
    p_est.add_argument("--target", type=float, default=25.0)
    p_est.add_argument("--json", action="store_true")
    p_est.set_defaults(func=_estimate)
    return parser


def _estimate(args: argparse.Namespace) -> None:
    from lsa import estimate as est

    if not args.counts.exists():
        raise SystemExit(f"counts parquet not found: {args.counts}")
    counts = est.read_counts(args.counts)
    passes = est.load_passes(args.passes)
    price = est.input_price(args.prices, args.model)
    out = est.estimate(counts, passes, price, target_usd=args.target)
    if args.json:
        print(json.dumps(asdict(out), indent=2))
    else:
        print(est.format_table(out))


def main() -> None:
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s %(message)s")
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
