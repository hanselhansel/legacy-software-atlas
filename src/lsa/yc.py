"""YC company list for the ``yc`` items family (plan 3, lane O).

``fetch_all`` downloads the yc-oss companies dump into a git-ignored cache
under ``data/raw/yc/``; ``--input`` reads a local file instead (tests and
re-runs never touch the network). ``company_rows`` keeps batches from 2024
onward and builds each item's text as the company one-liner plus long
description cut to the first 120 words.

``run`` writes ``data/derived/yc.parquet`` (item_id, slug, name, batch,
status) and upserts ``items.parquet`` rows with family ``yc`` plus one raw
JSON per item under ``data/raw/yc/`` so the ``yc: category`` Jev pass can
label them (see ``src/lsa/jev/items.py``).
"""

from __future__ import annotations

import hashlib
import json
import re
from datetime import UTC, datetime
from pathlib import Path

from lsa import paths
from lsa.fetch import common as fcommon

ALL_JSON = "https://yc-oss.github.io/api/companies/all.json"
SOURCE = "yc-oss"
FAMILY = "yc"
MIN_YEAR = 2024
TEXT_WORDS = 120

_YEAR4 = re.compile(r"(?:19|20)\d{2}")
_YEAR2 = re.compile(r"\b[WSF](\d{2})\b")


def batch_year(batch: str | None) -> int | None:
    """Year of a yc-oss batch string ("Winter 2024", "W24"), None if absent."""
    text = (batch or "").strip()
    m = _YEAR4.search(text)
    if m:
        return int(m.group(0))
    m = _YEAR2.search(text)
    if m:
        return 2000 + int(m.group(1))
    return None


def item_text(company: dict) -> str:
    """``one_liner`` + ``long_description``, first ``TEXT_WORDS`` words."""
    text = "\n\n".join(
        t
        for t in (company.get("one_liner"), company.get("long_description"))
        if t
    )
    return " ".join(text.split()[:TEXT_WORDS])


def item_id(company: dict) -> str:
    cid = company.get("id")
    return f"yc:{cid}" if cid is not None else f"yc:{company.get('slug', '')}"


def company_rows(
    companies: list[dict], *, min_year: int = MIN_YEAR
) -> list[dict]:
    """Kept companies (batch ``min_year`` on) with their item text."""
    rows = []
    for c in companies:
        year = batch_year(c.get("batch"))
        if year is None or year < min_year:
            continue
        text = item_text(c)
        if not text:
            continue
        rows.append(
            {
                "item_id": item_id(c),
                "slug": str(c.get("slug") or ""),
                "name": str(c.get("name") or ""),
                "batch": str(c.get("batch") or ""),
                "status": str(c.get("status") or ""),
                "url": str(c.get("url") or c.get("website") or ""),
                "text": text,
            }
        )
    return rows


def fetch_all(
    cache_path: Path, *, client=None, refresh: bool = False
) -> list[dict]:
    """The all.json list, from the cache when present (and not refreshing)."""
    from lsa.sources import http

    cache_path = Path(cache_path)
    if cache_path.exists() and not refresh:
        return json.loads(cache_path.read_text(encoding="utf-8"))
    own = client is None
    if own:
        client = http.make_client()
    try:
        resp = http.get_with_backoff(client, ALL_JSON)
        resp.raise_for_status()
        text = resp.text
        data = resp.json()
    finally:
        if own:
            client.close()
    if not isinstance(data, list):
        raise TypeError(f"{ALL_JSON}: expected a JSON list")
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(text, encoding="utf-8")
    return data


def write_yc(rows: list[dict], path: Path) -> Path:
    """yc.parquet: item_id, slug, name, batch, status per kept company."""
    import pyarrow as pa
    import pyarrow.parquet as pq

    schema = pa.schema(
        [
            ("item_id", pa.string()),
            ("slug", pa.string()),
            ("name", pa.string()),
            ("batch", pa.string()),
            ("status", pa.string()),
        ]
    )
    table = pa.Table.from_pylist(
        [
            {k: r[k] for k in ("item_id", "slug", "name", "batch", "status")}
            for r in rows
        ],
        schema=schema,
    )
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    pq.write_table(table, path)
    return path


def write_items(
    rows: list[dict],
    raw_dir: Path,
    items_path: Path,
    *,
    fetched_at: str,
) -> list[fcommon.ItemRow]:
    """Raw text JSON per kept company plus items.parquet rows (family yc)."""
    raw_dir = Path(raw_dir)
    out = []
    for r in rows:
        raw_dir.mkdir(parents=True, exist_ok=True)
        (raw_dir / f"{fcommon.safe_name(r['item_id'])}.json").write_text(
            json.dumps(
                {
                    "item_id": r["item_id"],
                    "source": SOURCE,
                    "url": r["url"],
                    "fetched_at": fetched_at,
                    "text": r["text"],
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        out.append(
            fcommon.ItemRow(
                item_id=r["item_id"],
                family=FAMILY,
                source=SOURCE,
                region="",
                category_hint="",
                url=r["url"],
                fetched_at=fetched_at,
                text_sha256=hashlib.sha256(r["text"].encode()).hexdigest(),
            )
        )
    if out:
        fcommon.append_items(out, items_path)
    return out


def run(
    *,
    input_path: Path | None = None,
    cache_path: Path | None = None,
    raw_dir: Path,
    items_path: Path,
    out_path: Path,
    fetched_at: str | None = None,
    refresh: bool = False,
    client=None,
    min_year: int = MIN_YEAR,
) -> list[dict]:
    """Load companies, keep recent batches, write the three outputs."""
    if input_path is not None:
        companies = json.loads(Path(input_path).read_text(encoding="utf-8"))
    else:
        companies = fetch_all(
            Path(cache_path or paths.RAW / "yc" / "all.json"),
            client=client,
            refresh=refresh,
        )
    rows = company_rows(companies, min_year=min_year)
    write_yc(rows, out_path)
    write_items(
        rows,
        raw_dir,
        items_path,
        fetched_at=fetched_at or datetime.now(UTC).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
    )
    return rows


def register(sub) -> None:
    p_yc = sub.add_parser(
        "yc", help="yc-oss company dump to items + yc.parquet (lane O)"
    )
    p_yc.add_argument(
        "--input",
        type=Path,
        default=None,
        help="local all.json; skips the download",
    )
    p_yc.add_argument(
        "--cache",
        type=Path,
        default=None,
        help="all.json cache path (default data/raw/yc/all.json)",
    )
    p_yc.add_argument(
        "--refresh",
        action="store_true",
        help="re-download even when the cache exists",
    )
    p_yc.add_argument(
        "--min-year",
        type=int,
        default=MIN_YEAR,
        help="keep batches from this year on (default: %(default)s)",
    )
    p_yc.add_argument(
        "--out",
        type=Path,
        default=None,
        help="yc parquet to write (default: data/derived/yc.parquet)",
    )
    p_yc.add_argument(
        "--items",
        type=Path,
        default=None,
        help="items parquet to upsert (default: data/derived/items.parquet)",
    )
    p_yc.add_argument(
        "--raw-dir",
        type=Path,
        default=None,
        help="raw item dir (default: data/raw/yc)",
    )
    p_yc.add_argument(
        "--dry-run",
        action="store_true",
        help="count kept companies; no writes",
    )
    p_yc.set_defaults(func=_yc)


def _yc(args) -> None:
    if args.dry_run:
        if args.input is not None:
            companies = json.loads(args.input.read_text(encoding="utf-8"))
        else:
            companies = fetch_all(
                args.cache or paths.RAW / "yc" / "all.json"
            )
        rows = company_rows(companies, min_year=args.min_year)
        by_batch: dict[str, int] = {}
        for r in rows:
            by_batch[r["batch"]] = by_batch.get(r["batch"], 0) + 1
        for batch in sorted(by_batch):
            print(f"{batch:<14} {by_batch[batch]}")
        print(
            f"dry run: {len(rows)} companies in {args.min_year}+ batches, "
            "nothing written"
        )
        return
    rows = run(
        input_path=args.input,
        cache_path=args.cache,
        raw_dir=args.raw_dir or paths.RAW / "yc",
        items_path=args.items or paths.DERIVED / "items.parquet",
        out_path=args.out or paths.DERIVED / "yc.parquet",
        refresh=args.refresh,
        min_year=args.min_year,
    )
    print(f"wrote {len(rows)} yc companies (batches {args.min_year}+)")
