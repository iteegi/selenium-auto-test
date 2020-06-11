"""Wait."""

from . __private.__wait import __web_driver_wait

from patterns.generating.factory_method import FactoryMethod
from selenium.webdriver.support.wait import WebDriverWait as WDW


# FIXME убрать метод
def web_driver_wait(*args, **kwargs):
    """Get web driver wait."""
    return __web_driver_wait(*args, **kwargs)


@FactoryMethod
class WebDriverWait():
    """Factory Method for WebDriverWait from Selenium."""

    WDWSelenium = WDW
