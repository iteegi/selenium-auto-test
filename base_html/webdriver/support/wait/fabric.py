"""Factory Methods for wait from external sources."""

from patterns.generating.factory_method import FactoryMethod
from selenium.webdriver.support.wait import WebDriverWait as WDW


@FactoryMethod
class WebDriverWait():
    """Factory Method for WebDriverWait from Selenium."""

    WDW_SELENIUM = WDW
