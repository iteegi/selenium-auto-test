"""Custom expected conditions."""

from typing import Type, Tuple, List

from base_html.webdriver.support.ec.interfaces.iec import IExpectedConditions
from base_html.webdriver.remote.webdriver.fabric import BaseWebDriverFabric
from base_html.webdriver.remote.webelement.fabric import BaseWebElementFabric

base_webdriver = Type[BaseWebDriverFabric.REMOTE_WEB_DRIVER_SELENIUM]
base_webelement = Type[BaseWebElementFabric.REMOTE_WEB_ELEMENT_SELENIUM]


class ElementLocatedCascade(IExpectedConditions):
    """Find an element inside another element."""

    def __init__(self,
                 target: Tuple[str, str],
                 locator: Tuple[str, str]) -> None:
        """Initialize.

        target - selector where you want to find another element
        locator - element selector
        """
        self.__target = target
        self.__locator = locator

    def __call__(self,
                 driver: base_webdriver) -> base_webelement:
        """Call when an instance is "called" as a function.

        In the Until method of the WebDriverWait class.
        """
        return driver.find_element(
            *self.__target).find_element(
                *self.__locator)


class ElementsLocatedCascade(IExpectedConditions):
    """Find an elements inside another element."""

    def __init__(self,
                 target: Tuple[str, str],
                 locator: Tuple[str, str]) -> None:
        """Initialize.

        target - selector where you want to find another elements
        locator - elements selector
        """
        self.__target = target
        self.__locator = locator

    def __call__(self,
                 driver: base_webdriver) -> List[base_webelement]:
        """Call when an instance is "called" as a function.

        In the Until method of the WebDriverWait class.
        """
        return driver.find_element(
            *self.__target).find_elements(
                *self.__locator)
