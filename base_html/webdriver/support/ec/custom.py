"""Custom methods implementing expected conditions."""

# TODO: избавиться от селениум
from selenium.webdriver.remote.webdriver import WebDriver


class ExecScriptReturnZero(object):
    """The supplied external script returns zero."""

    def __init__(self, script: str) -> None:
        """Initialize."""
        self._script = script

    def __call__(self, driver:  WebDriver) -> bool:
        """Call when the instance is “called” as a function."""
        element: int = driver.execute_script(self._script)
        if element == 0:
            return True
        else:
            return False
