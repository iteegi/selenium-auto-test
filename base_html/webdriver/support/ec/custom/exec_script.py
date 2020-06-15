"""Custom methods implementing expected conditions."""

from typing import Type

from base_html.webdriver.support.ec.interfaces.iec import IExpectedConditions
from base_html.webdriver.remote.webdriver.fabric import BaseWebDriverFabric

base_webdriver = Type[BaseWebDriverFabric.REMOTE_WEB_DRIVER_SELENIUM]


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
