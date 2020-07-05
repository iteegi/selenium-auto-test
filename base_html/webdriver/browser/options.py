"""Optipons."""

from selenium.webdriver.chrome.options import Options as options

from patterns.generating.factory_method import FactoryMethod


@FactoryMethod
class Options():
    """Factory Method for Options from Selenium."""

    Options_SELENIUM = options
