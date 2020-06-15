"""Factory Method for base class Web Driver."""


from selenium.webdriver.remote.webdriver import WebDriver
from patterns.generating.factory_method import FactoryMethod

# TODO: возможно это не самый лучший способ для аннотации базового класса
# для webdriver'a
@FactoryMethod
class BaseWebDriverFabric():
    """Factory Method for base class Web Driver."""

    REMOTE_WEB_DRIVER_SELENIUM = WebDriver
