"""Custom expected conditions."""

from typing import Type

from base_html.webdriver.support.ec.interfaces.iec import IExpectedConditions
from base_html.webdriver.remote.webdriver.fabric import BaseWebDriverFabric

base_webdriver = Type[BaseWebDriverFabric.REMOTE_WEB_DRIVER_SELENIUM]


class ElementLocatedCascade(IExpectedConditions):
    """Find an element inside another element.

    target - selector where you want to find another element
    locator - element selector
    """

    def __init__(self, target, locator):
        """Initialize."""
        self.__target = target
        self.__locator = locator

    def __call__(self, driver):
        """Call when an instance is "called" as a function.

        In the Until method of the WebDriverWait class.
        """
        return driver.find_element(
            *self.__target).find_element(
                *self.__locator)
