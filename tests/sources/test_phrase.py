"""Tests for the exact-phrase query shapers shared by API counters."""

from __future__ import annotations

from lsa.sources import phrase


def test_quoted_wraps_multiword_query():
    assert phrase.quoted("core banking") == '"core banking"'


def test_quoted_keeps_special_chars_literal():
    assert phrase.quoted("z/TPF d'art & sons") == '"z/TPF d\'art & sons"'


def test_quoted_strips_embedded_double_quotes():
    assert phrase.quoted('say "hi" there') == '"say hi there"'


def test_quoted_returns_none_for_empty():
    assert phrase.quoted("") is None
    assert phrase.quoted("   ") is None


def test_escaped_quotes_and_escapes_specials():
    out = phrase.escaped("z/TPF")
    assert out == '"z\\/TPF"'


def test_escaped_multiword_with_apostrophe():
    out = phrase.escaped("SAP FI/CO Berater d'art")
    assert out == '"SAP FI\\/CO Berater d\'art"'


def test_escaped_returns_none_for_empty():
    assert phrase.escaped("") is None
