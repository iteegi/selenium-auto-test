"""Different functions."""


def exec_func_several_times(func, quantity=1):
    """Execute a function several times."""
    for i in range(quantity):
        func()
