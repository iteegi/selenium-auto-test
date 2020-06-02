import pytest


# @pytest.fixture(params=[1, 2, None])
# def fix(request):
#     yield request.param
#
#
# def test_f(fix):
#     print(fix)
#
# @pytest.fixture(params=[0, 1], ids=["spam", "ham"])
# def a(request):
#     return request.param
#
#
# def test_a(a):
#     pass
#
#
# def idfn(fixture_value):
#     print("---> {0}".format(fixture_value))
#     if fixture_value == 0:
#         return "eggs"
#     else:
#         return None
#
#
# @pytest.fixture(params=[0, 1, 8], ids=idfn)
# def b(request):
#     return request.param
#
#
# def test_b(b):
#     pass
#
# @pytest.fixture(params=[0, 1, pytest.param(2, marks=pytest.mark.skip)])
# def data_set(request):
#     return request.param
#
#
# def test_data(data_set):
#     pass

@pytest.fixture(scope="module", params=["mod1", "mod2"])
def modarg(request):
    param = request.param
    print("  SETUP modarg", param)
    yield param
    print("  TEARDOWN modarg", param)


@pytest.fixture(scope="function", params=[1, 2])
def otherarg(request):
    param = request.param
    print("  SETUP otherarg", param)
    yield param
    print("  TEARDOWN otherarg", param)


def test_0(otherarg):
    print("  RUN test0 with otherarg", otherarg)


def test_1(modarg):
    print("  RUN test1 with modarg", modarg)


def test_2(otherarg, modarg):
    print("  RUN test2 with otherarg {} and modarg {}".format(otherarg, modarg))
