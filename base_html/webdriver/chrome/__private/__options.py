"""Selenium options."""

from selenium.webdriver.chrome.options import Options


def __get_options(*args, **kwargs):
    return Options(*args, **kwargs)
