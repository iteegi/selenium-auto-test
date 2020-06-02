import pytest

def determine_scope(fixture_name, config):
    print("---> {0}".format(fixture_name))
    if config.getoption("--keep-containers", None):
        return "session"
    return "function"


@pytest.fixture(scope=determine_scope)
def docker_container():
    yield spawn_container()

order = []


@pytest.fixture(scope="session")
def s1():
    order.append("s1")


@pytest.fixture(scope="module")
def m1():
    order.append("m1")


@pytest.fixture
def f1(f3):
    order.append("f1")


@pytest.fixture
def f3():
    order.append("f3")


@pytest.fixture(autouse=True)
def a1():
    order.append("a1")


@pytest.fixture
def f2():
    order.append("f2")


# @pytest.mark.xfail()
def test_order(f1, m1, f2, s1):
    print(order)
    assert order == ["s1", "m1", "a1", "f3", "f1", "f2"]
