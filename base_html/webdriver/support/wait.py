"""Wait."""

from . __private.__wait import __web_driver_wait


def web_driver_wait(*args, **kwargs):
    """Get web driver wait."""
    return __web_driver_wait(*args, **kwargs)
