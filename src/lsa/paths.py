"""Repository-relative locations. data/raw/ is gitignored; data/derived/ holds
tracked parquet tables.

Read these as `paths.X` at call time (never `from lsa.paths import X`) so tests can
monkeypatch them.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw"
DERIVED = ROOT / "data" / "derived"
RESEARCH = ROOT / "research"
