"""Unit tests."""
from molecule import api


def test_verifier_is_detected(VERIFIER):
    """Asserts that molecule recognizes the verifier."""
    assert VERIFIER in [str(d) for d in api.verifiers()]
