"""Sync JevClient: retries, attempt visibility, validation, endpoint safety."""

import pytest

from lsa.jev.client import (
    JevClient,
    ModelMismatch,
    RetryPolicy,
    UnsafeEndpoint,
)
from lsa.jev.keys import MissingKey, base_url, get_api_key
from tests.jev.mock_jev import make_transport

CANARY = "apikey_" + "0" * 36 + "_" + "f" * 64
Q = {"q": {"type": "noul", "instructions": "Is `i1` a problem?"}}
Q_CHOICE = {
    "c": {"type": "choice", "instructions": "?", "criteria": {"a": "A", "b": "B"}}
}


def evaluate(script, questions=Q, max_attempts=4, on_attempt=None, seen=None):
    client = JevClient(
        api_key=CANARY,
        base="http://mock",
        transport=make_transport(script, seen),
        policy=RetryPolicy(
            max_attempts=max_attempts, backoff_initial=0, backoff_max=0
        ),
    )
    try:
        return client.evaluate({"i1": "x"}, questions, model="jev-1.13.0",
                               on_attempt=on_attempt)
    finally:
        client.close()


def test_success_records_one_attempt_with_request_id_and_usage():
    seen = []
    res = evaluate(["ok"], seen=seen)
    assert res.ok and len(res.attempts) == 1
    a = res.attempts[0]
    assert (a.http_status, a.request_id, a.input_tokens, a.model_returned) == (
        200,
        "req_0001",
        300,
        "jev-1.13.0",
    )
    assert seen[0].headers["authorization"] == f"Bearer {CANARY}"


def test_retries_are_visible_as_separate_attempts():
    res = evaluate(["429", "529", "ok"])
    assert res.ok and [a.http_status for a in res.attempts] == [429, 529, 200]
    assert [a.error_type for a in res.attempts] == [
        "rate_limited",
        "overloaded",
        None,
    ]


def test_timeout_is_an_unknown_charge_not_free():
    res = evaluate(["timeout", "ok"])
    assert res.attempts[0].error_type == "timeout"
    assert res.attempts[0].charge_known is False
    assert res.attempts[1].charge_known is True


def test_null_usage_marks_charge_unknown_but_keeps_answers():
    res = evaluate(["null_usage"])
    assert res.ok
    assert res.attempts[0].input_tokens is None
    assert res.attempts[0].charge_known is False


def test_non_retryable_422_stops():
    res = evaluate(["422"])
    assert not res.ok and len(res.attempts) == 1
    assert res.attempts[0].error_type == "invalid_request"
    assert res.attempts[0].charge_known is True
    assert res.invalid is False


def test_auth_failure_never_retried():
    res = evaluate(["401"])
    assert not res.ok and len(res.attempts) == 1
    assert res.attempts[0].error_type == "auth"


def test_bad_choice_is_schema_failure_retried_once():
    res = evaluate(["bad_choice", "bad_choice", "ok"], questions=Q_CHOICE)
    assert not res.ok and res.invalid
    assert [a.validation for a in res.attempts] == ["schema", "schema"]


def test_bad_choice_then_ok_succeeds():
    res = evaluate(["bad_choice", "ok"], questions=Q_CHOICE)
    assert res.ok and len(res.attempts) == 2


def test_missing_question_fails_schema():
    res = evaluate(["missing_question", "missing_question"], questions=Q_CHOICE)
    assert not res.ok and res.invalid


def test_wrong_model_raises():
    with pytest.raises(ModelMismatch):
        evaluate(["wrong_model"])


def test_on_attempt_fires_before_and_after():
    phases = []
    evaluate(["429", "ok"], on_attempt=lambda ev: phases.append(ev.phase))
    assert phases == [
        "before_send",
        "after_response",
        "before_send",
        "after_response",
    ]


def test_non_production_base_requires_canary_key():
    with pytest.raises(UnsafeEndpoint):
        JevClient(api_key="apikey_" + "1" * 36 + "_" + "e" * 64, base="http://mock")


def test_production_base_accepts_real_key_shape():
    client = JevClient(
        api_key="apikey_" + "1" * 36 + "_" + "e" * 64,
        base="https://api.typesafe.ai",
        transport=make_transport([]),
    )
    client.close()


def test_keys_from_env_only(monkeypatch):
    monkeypatch.setenv("TYPESAFE_API_KEY", CANARY)
    assert get_api_key() == CANARY
    monkeypatch.delenv("TYPESAFE_API_KEY")
    with pytest.raises(MissingKey):
        get_api_key()


def test_base_url_env_and_default(monkeypatch):
    monkeypatch.delenv("TYPESAFE_BASE_URL", raising=False)
    assert base_url() == "https://api.typesafe.ai"
    monkeypatch.setenv("TYPESAFE_BASE_URL", "http://127.0.0.1:9/")
    assert base_url() == "http://127.0.0.1:9"
