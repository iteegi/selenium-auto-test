
import pytest


class A():
    pass


@pytest.fixture(params=[1, 2])
def f():
    return A()


def test_f(f):
    print(f)


class TestClass:
    def test_1(self):
        x = "this"
        assert "h" in x

    def test_2(self):
        assert hasattr(str, "__init__")


class TestC:
    def test_3(self):
        assert "a" == "b", "---> Super description <---"
