"""Selenium wait."""

from selenium.webdriver.support.wait import WebDriverWait


def __web_driver_wait(*args, **kwargs):
    return WebDriverWait(*args, **kwargs)
