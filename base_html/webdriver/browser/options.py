"""Optipons."""

from . __private.__options import __get_options


def options(*args, **kwargs):
    """Get options."""
    return __get_options(*args, **kwargs)
