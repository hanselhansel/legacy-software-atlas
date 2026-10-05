"""Question sets from configs/questions.toml, and packed-call building.

One set per ``[[pass]]`` in configs/passes.toml, keyed by the pass name. Config
question types use spec vocabulary (``choice``, ``score``, ``probability``);
the wire carries TypeSafe types, so ``probability`` maps to ``noul``.

Packed calls send ``items_per_call`` items at once: state slots ``i1``..``ik``
hold the text windows, and every question is copied per slot as ``i{j}_{qid}``
with `` `item` `` references rewritten to `` `i{j}` `` (the pattern is ported
from jev-opportunity-atlas ``inference.questions`` and ``pilot.packed``).
"""

from __future__ import annotations

import copy
import hashlib
import json
import re
import tomllib
from dataclasses import dataclass
from pathlib import Path

from lsa import paths

CONFIG_TYPES = frozenset({"choice", "score", "probability"})
WIRE_TYPE = {"probability": "noul"}  # spec vocabulary -> TypeSafe type
ITEM_REF = "`item`"


def canonical_json(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def slugify(pass_name: str) -> str:
    """Pass name -> config/ledger key: lowercase, non-alnum runs become '-'."""
    slug = re.sub(r"[^a-z0-9]+", "-", pass_name.lower()).strip("-")
    if not slug:
        raise ValueError(f"pass name {pass_name!r} has no usable slug")
    return slug


@dataclass(frozen=True)
class QuestionSet:
    pass_name: str
    slug: str
    version: int
    label: str  # "<slug>@v<version>"
    questions: dict  # config-typed question dicts
    sha256: str  # canonical {name, version, questions} hash


def _check(set_name: str, qid: str, q: dict) -> None:
    qtype = q.get("type")
    if qtype not in CONFIG_TYPES:
        raise ValueError(
            f"{set_name}.{qid}: bad type {qtype!r} (one of {sorted(CONFIG_TYPES)})"
        )
    criteria = q.get("criteria")
    if qtype == "choice" and not isinstance(criteria, dict):
        raise ValueError(f"{set_name}.{qid}: choice needs a criteria table")
    if qtype == "score" and not isinstance(criteria, list):
        raise ValueError(f"{set_name}.{qid}: score needs a criteria list")
    if qtype == "probability" and criteria is not None:
        raise ValueError(f"{set_name}.{qid}: probability takes no criteria")


def question_sets(path: Path) -> dict[str, QuestionSet]:
    """All sets in a questions.toml, keyed by pass name; slug collisions raise."""
    data = tomllib.loads(Path(path).read_text(encoding="utf-8"))
    out: dict[str, QuestionSet] = {}
    for name, spec in data.items():
        questions = spec.get("questions") or {}
        for qid, q in questions.items():
            _check(name, qid, q)
        slug = slugify(name)
        if any(s.slug == slug for s in out.values()):
            raise ValueError(f"pass name {name!r} collides on slug {slug!r}")
        version = int(spec.get("version", 1))
        digest = hashlib.sha256(
            canonical_json(
                {"name": name, "version": version, "questions": questions}
            ).encode("utf-8")
        ).hexdigest()
        out[name] = QuestionSet(
            name, slug, version, f"{slug}@v{version}", questions, digest
        )
    return out


def question_set(pass_name: str, path: Path | None = None) -> QuestionSet:
    """The set for one pass name; unknown names raise with the valid list."""
    sets = question_sets(path or paths.ROOT / "configs" / "questions.toml")
    try:
        return sets[pass_name]
    except KeyError:
        raise KeyError(
            f"no question set for pass {pass_name!r} (have: {sorted(sets)})"
        ) from None


def _slot_question(question: dict, slot: str) -> dict:
    """Wire copy of one question for slot `i{j}`: type mapped, `item` -> slot."""
    q = copy.deepcopy(question)
    q["type"] = WIRE_TYPE.get(q["type"], q["type"])
    if isinstance(q.get("instructions"), str):
        q["instructions"] = q["instructions"].replace(ITEM_REF, f"`{slot}`")
    criteria = q.get("criteria")
    if isinstance(criteria, dict):
        q["criteria"] = {
            key: (
                value.replace(ITEM_REF, f"`{slot}`")
                if isinstance(value, str)
                else value
            )
            for key, value in criteria.items()
        }
    return q


def pack_questions(qs: QuestionSet, k: int) -> dict:
    """Wire questions for a pack of k members: ``i{j}_{qid}`` per slot."""
    return {
        f"i{j}_{qid}": _slot_question(q, f"i{j}")
        for j in range(1, k + 1)
        for qid, q in qs.questions.items()
    }


def pack_state(members: list[dict]) -> dict:
    """Packed state: ``{i1: text, ..., ik: text}`` over member dicts."""
    return {f"i{j}": str(m["text"]) for j, m in enumerate(members, start=1)}


def request_body(state: dict, questions: dict, model: str) -> dict:
    return {"state": state, "model": model, "questions": questions}


def pack_body(members: list[dict], qs: QuestionSet, model: str) -> dict:
    """Full request body for one packed call."""
    return request_body(
        pack_state(members), pack_questions(qs, len(members)), model
    )


SLOT_QID = re.compile(r"^i(\d+)_(.+)$")


def unpack_answers(questions: dict, answers: dict, members: list[dict]) -> dict:
    """``{item_id: {qid: answer}}`` from packed ``i{j}_{qid}`` wire answers."""
    out: dict[str, dict] = {}
    for wire_qid, a in answers.items():
        m = SLOT_QID.match(wire_qid)
        if m is None:
            continue
        member = members[int(m.group(1)) - 1]
        out.setdefault(str(member["item_id"]), {})[m.group(2)] = a
    return out
