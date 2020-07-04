"""Webdrivers."""

from selenium.webdriver import Chrome

from patterns.generating.factory_method import FactoryMethod


@FactoryMethod
class WebDriver():
    """Factory Method for Chrome from Selenium."""

    CHROME_SELENIUM = Chrome
