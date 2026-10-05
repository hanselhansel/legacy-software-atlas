"""Per-pass run state: run dir, run_manifest.json, done.jsonl, answer parts.

Layout under ``data/derived/jev/<slug>/`` (pilot runs use ``<slug>-pilot``):

- ``run_manifest.json`` pins model and question-set hashes; a later run with a
  different model, or the same question-set label at a different hash, is
  refused (ported from jev-opportunity-atlas ``inference.runner_io``).
- ``done.jsonl`` rows are appended only after the answer part is fsynced and
  renamed; a done row whose part is gone is dropped so the item is redone.
- ``answers/part-<seq>.parquet`` parts are atomic (tmp + fsync + rename) and
  never overwritten; seq = 1 + max existing.
"""

from __future__ import annotations

import json
import os
import subprocess
from datetime import UTC, datetime
from pathlib import Path

from lsa import paths
from lsa.jev.questions import canonical_json


class ManifestMismatch(RuntimeError):
    pass


class PartExists(RuntimeError):
    pass


def _utcnow() -> str:
    return datetime.now(UTC).isoformat()


def run_dir(slug: str, root: Path | None = None) -> Path:
    base = Path(root) if root is not None else paths.DERIVED / "jev"
    return base / slug


def _answers_schema():
    import pyarrow as pa

    return pa.schema(
        [
            ("run_id", pa.string()),
            ("item_id", pa.string()),
            ("question_set", pa.string()),
            ("question_id", pa.string()),
            ("qtype", pa.string()),
            ("probability", pa.float64()),
            ("choice", pa.string()),
            ("score", pa.float64()),
            ("probabilities_json", pa.string()),
            ("confidence", pa.float64()),
            ("model_returned", pa.string()),
            ("request_id", pa.string()),
            ("logical_call_id", pa.string()),
        ]
    )


def answer_rows(
    run_id: str,
    item_id: str,
    qs,
    answers: dict,
    model_returned: str | None,
    request_id: str | None,
    logical_call_id: str,
) -> list[dict]:
    """One ANSWERS row per config question, in question order. ``qtype`` is the
    spec type (choice/score/probability); the wire ``noul`` value lands in the
    ``probability`` column."""
    rows = []
    for qid, q in qs.questions.items():
        a = answers.get(qid) or {}
        probs = a.get("probabilities")
        rows.append(
            {
                "run_id": run_id,
                "item_id": str(item_id),
                "question_set": qs.label,
                "question_id": qid,
                "qtype": q.get("type"),
                "probability": a.get("noul"),
                "choice": a.get("choice"),
                "score": a.get("score"),
                "probabilities_json": canonical_json(probs)
                if probs is not None
                else None,
                "confidence": a.get("confidence"),
                "model_returned": model_returned,
                "request_id": request_id,
                "logical_call_id": logical_call_id,
            }
        )
    return rows


def _git_commit() -> str | None:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=paths.ROOT,
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    return out.stdout.strip() or None


def _atomic_write_json(path: Path, obj) -> None:
    tmp = path.with_name(path.name + ".tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=1)
        fh.write("\n")
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)


def ensure_manifest(dir: Path, qs, model: str, price_version: str, cap_usd: float) -> None:
    """Write run_manifest.json on first use of the dir; refuse a different
    model or a changed question-set hash on later runs."""
    path = dir / "run_manifest.json"
    entry = {"label": qs.label, "file_sha256": qs.sha256}
    if not path.exists():
        _atomic_write_json(
            path,
            {
                "pass": qs.slug,
                "model": model,
                "question_sets": [entry],
                "price_version": price_version,
                "cap_usd": cap_usd,
                "git_commit": _git_commit(),
                "started_at": _utcnow(),
            },
        )
        return
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if manifest.get("model") != model:
        raise ManifestMismatch(
            f"{path}: model is {manifest.get('model')!r}, run wants {model!r}"
        )
    known = {e["label"]: e for e in manifest.get("question_sets", [])}
    if qs.label in known:
        if known[qs.label].get("file_sha256") != qs.sha256:
            raise ManifestMismatch(
                f"{path}: question set {qs.label} hash changed"
            )
        return
    manifest.setdefault("question_sets", []).append(entry)
    _atomic_write_json(path, manifest)


def load_done(dir: Path, question_set: str) -> set[str]:
    """Item ids already completed for this question set. A done row whose
    answer part is gone is dropped (the item is redone)."""
    done: set[str] = set()
    path = dir / "done.jsonl"
    if not path.exists():
        return done
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row.get("question_set") != question_set:
            continue
        if (dir / "answers" / f"part-{row['part']}.parquet").exists():
            done.add(str(row["item_id"]))
    return done


def append_done(dir: Path, entries: list[dict]) -> None:
    path = dir / "done.jsonl"
    with open(path, "a", encoding="utf-8") as fh:
        fh.writelines(json.dumps(e, ensure_ascii=False) + "\n" for e in entries)
        fh.flush()
        os.fsync(fh.fileno())


def _fsync_dir(path: Path) -> None:
    fd = os.open(path, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def write_part(dir: Path, rows: list[dict]) -> int:
    """Write ``answers/part-<seq>.parquet`` atomically; parts never overwrite."""
    import pyarrow as pa
    import pyarrow.parquet as pq

    answers_dir = dir / "answers"
    answers_dir.mkdir(parents=True, exist_ok=True)
    for stale in answers_dir.glob("part-*.parquet.tmp"):
        stale.unlink()  # crash leftovers; only *.parquet may remain
    seqs = [
        int(p.stem.rsplit("-", 1)[1]) for p in answers_dir.glob("part-*.parquet")
    ]
    seq = 1 + max(seqs, default=0)
    tmp = answers_dir / f"part-{seq}.parquet.tmp"
    final = answers_dir / f"part-{seq}.parquet"
    if final.exists():
        raise PartExists(f"{final} already exists")
    table = pa.Table.from_pylist(rows, schema=_answers_schema())
    pq.write_table(table, str(tmp))
    fd = os.open(tmp, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)
    if final.exists():
        raise PartExists(f"{final} already exists")
    os.rename(tmp, final)
    _fsync_dir(answers_dir)
    return seq
