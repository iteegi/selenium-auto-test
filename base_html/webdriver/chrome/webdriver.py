"""Webdriver."""

from . __private.__webdriver import __get_chrome_wd


def chrome(*args, **kwargs):
    """Get Chrome webdriver."""
    return __get_chrome_wd(*args, **kwargs)
