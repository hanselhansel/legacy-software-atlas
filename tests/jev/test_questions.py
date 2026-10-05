"""Question sets: config loading, slugs, packing (plan 2, task 2)."""

from pathlib import Path

import pytest

from lsa import estimate as est
from lsa.jev import questions as jq

ROOT = Path(__file__).resolve().parents[2]
QUESTIONS = ROOT / "configs" / "questions.toml"
PASSES = ROOT / "configs" / "passes.toml"


def test_every_pass_has_a_question_set():
    pass_names = {p.name for p in est.load_passes(PASSES)}
    sets = jq.question_sets(QUESTIONS)
    assert pass_names == set(sets)
    for qs in sets.values():
        assert qs.version >= 1
        assert qs.label == f"{qs.slug}@v{qs.version}"
        assert len(qs.sha256) == 64
        assert qs.questions


def test_slugs_are_unique_and_stable():
    assert jq.slugify("tenders: which category") == "tenders-which-category"
    assert (
        jq.slugify("vendor stories: category, in use or replaced, segment, region")
        == "vendor-stories-category-in-use-or-replaced-segment-region"
    )
    sets = jq.question_sets(QUESTIONS)
    assert len({s.slug for s in sets.values()}) == len(sets)


def test_question_types_and_criteria():
    for qs in jq.question_sets(QUESTIONS).values():
        for qid, q in qs.questions.items():
            assert q["type"] in {"choice", "score", "probability"}, qid
            if q["type"] == "choice":
                assert isinstance(q["criteria"], dict) and q["criteria"], qid
            if q["type"] == "probability":
                assert "criteria" not in q, qid


def test_category_choices_match_kept_categories():
    import csv

    with open(ROOT / "research" / "categories.csv", newline="") as fh:
        kept = [
            r["slug"] for r in csv.DictReader(fh) if r["kept"] == "True"
        ]
    qs = jq.question_set("tenders: which category", QUESTIONS)
    options = qs.questions["category"]["criteria"]
    assert kept, "categories.csv has no kept rows"
    assert all(k in options for k in kept)
    assert {"other", "unclear"} <= set(options)


def test_reasons_match_spec_question_4():
    qs = jq.question_set("HN: firsthand pain and reason to stay", QUESTIONS)
    options = qs.questions["reason_to_stay"]["criteria"]
    assert {"regulation", "switching_cost", "contracts", "skills", "data"} <= set(
        options
    )


def test_unknown_pass_raises_with_valid_names():
    with pytest.raises(KeyError, match="no question set"):
        jq.question_set("nope", QUESTIONS)


def test_invalid_config_rejected(tmp_path):
    cfg = tmp_path / "q.toml"
    cfg.write_text(
        '["p: x"]\nversion = 1\n'
        '["p: x".questions.q]\ntype = "choice"\ninstructions = "i"\n',
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="criteria table"):
        jq.question_sets(cfg)


def test_pack_rewrites_item_refs_and_maps_types():
    qs = jq.question_set("HN: firsthand pain and reason to stay", QUESTIONS)
    members = [
        {"item_id": "a1", "text": "we still reconcile by hand"},
        {"item_id": "a2", "text": "the contract runs to 2031"},
    ]
    body = jq.pack_body(members, qs, "jev-1.13.0")
    assert body["state"] == {
        "i1": "we still reconcile by hand",
        "i2": "the contract runs to 2031",
    }
    questions = body["questions"]
    assert set(questions) == {
        "i1_firsthand_pain",
        "i1_reason_to_stay",
        "i2_firsthand_pain",
        "i2_reason_to_stay",
    }
    assert questions["i1_firsthand_pain"]["type"] == "noul"
    assert "`i1`" in questions["i1_firsthand_pain"]["instructions"]
    assert "`item`" not in questions["i1_firsthand_pain"]["instructions"]
    assert "`i2`" in questions["i2_reason_to_stay"]["instructions"]


def test_unpack_answers_maps_slots_to_items():
    qs = jq.question_set("HN: firsthand pain and reason to stay", QUESTIONS)
    members = [{"item_id": 10, "text": "x"}, {"item_id": 20, "text": "y"}]
    answers = {
        "i1_firsthand_pain": {"type": "noul", "noul": 0.9},
        "i1_reason_to_stay": {"type": "choice", "choice": "skills"},
        "i2_firsthand_pain": {"type": "noul", "noul": 0.1},
        "i2_reason_to_stay": {"type": "choice", "choice": "contracts"},
    }
    out = jq.unpack_answers(jq.pack_questions(qs, 2), answers, members)
    assert out["10"]["firsthand_pain"]["noul"] == 0.9
    assert out["20"]["reason_to_stay"]["choice"] == "contracts"


def test_pack_single_member_uses_i1():
    qs = jq.question_set(
        "tenders: legacy system in use, being replaced, or neither", QUESTIONS
    )
    body = jq.pack_body([{"item_id": "x", "text": "t"}], qs, "jev-1.13.0")
    assert body["state"] == {"i1": "t"}
    assert set(body["questions"]) == {"i1_system_status"}
