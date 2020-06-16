"""base_html code execptions."""

from patterns.generating.factory_method import FactoryMethod

from selenium.common import exceptions


@FactoryMethod
class ExceptionFabric():
    """Factory Method for code execptions from Selenium."""

    EXCEPTIONS_SELENIUM = exceptions
