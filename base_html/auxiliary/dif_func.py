"""Different functions."""

from typing import Callable


def exec_func_several_times(func: Callable[[], None],
                            quantity: int = 1) -> None:
    """Execute a function several times."""
    for i in range(quantity):
        func()
