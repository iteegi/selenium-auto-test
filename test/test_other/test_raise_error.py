import pytest


def test_mytest():
    with pytest.raises(SystemExit):
        raise SystemExit
        # raise ZeroDivisionError


def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()


@pytest.mark.xfail(raises=ValueError)
def test_f():
    myfunc()
