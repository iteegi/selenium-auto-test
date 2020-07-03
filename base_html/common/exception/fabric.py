"""base_html code execptions."""

from selenium.common import exceptions

from patterns.generating.factory_method import FactoryMethod


@FactoryMethod
class Exceptions():
    """Factory Method for code execptions from Selenium."""

    EXCEPTIONS_SELENIUM = exceptions
