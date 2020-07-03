"""Factory method for By class."""

from selenium.webdriver.common.by import By as by
from patterns.generating.factory_method import FactoryMethod


@FactoryMethod
class By():
    """Factory Method for base class By."""

    BY_SELENIUM = by
