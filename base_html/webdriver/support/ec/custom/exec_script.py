"""Custom methods implementing expected conditions."""

from typing import Type

from base_html.webdriver.support.ec.interfaces.iec import IExpectedConditions
from base_html.webdriver.remote.webdriver.fabric import BaseWebDriverFabric
from base_html.webdriver.remote.webelement.fabric import BaseWebElementFabric

base_webdriver = Type[BaseWebDriverFabric.REMOTE_WEB_DRIVER_SELENIUM]
base_webelement = Type[BaseWebElementFabric.REMOTE_WEB_ELEMENT_SELENIUM]


class ExecScriptReturnZero(IExpectedConditions):
    """The supplied external script returns zero."""

    def __init__(self, script: str) -> None:
        """Initialize.

        script - code to be executed on the page. Code should return a number.
        """
        self._script = script

    def __call__(self,
                 driver: base_webdriver) -> bool:
        """Call when an instance is "called" as a function.

        In the Until method of the WebDriverWait class.
        """
        element: int = driver.execute_script(self._script)
        if element == 0:
            return True
        else:
            return False


class ScrollToElement():
    """Scroll to the specified item."""

    def __init__(self,
                 element: base_webelement) -> None:
        """Initialize.

        element - item to scroll to.
        """
        self.__element = element

    def __call__(self,
                 driver: base_webdriver,) -> bool:
        """Call when an instance is "called" as a function.

        In the Until method of the WebDriverWait class.
        """
        target = self.__element.location['y']
        script = f"window.scroll(0, {target});\
                    return window.pageYOffset"
        scroll: int = driver.execute_script(script)

        if target == scroll:
            return True
        else:
            return False
