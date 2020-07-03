"""Factory method for By class."""

from selenium.webdriver.common.keys import Keys as keys
from patterns.generating.factory_method import FactoryMethod


@FactoryMethod
class Keys():
    """Factory Method for base class Web Driver."""

    KEYS_SELENIUM = keys
