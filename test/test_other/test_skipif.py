import pytest

minversion = pytest.mark.skipif(
    50 < 70, reason="text"
)


@minversion
def test_function():
    pass
