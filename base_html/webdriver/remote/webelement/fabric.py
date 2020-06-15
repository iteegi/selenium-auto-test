"""Factory Method for Web Element."""

from selenium.webdriver.remote.webdriver import WebElement
from patterns.generating.factory_method import FactoryMethod


@FactoryMethod
class BaseWebElementFabric():
    """Factory Method for Web Element."""

    REMOTE_WEB_ELEMENT_SELENIUM = WebElement
