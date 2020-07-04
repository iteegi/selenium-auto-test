"""TextToBePresentInElement."""

from typing import Type, Tuple

from .interfaces.icheckertext import ICheckText

from base_html.webdriver.remote.webdriver.fabric import BaseWebDriverFabric
from base_html.webdriver.support.wait.fabric import WebDriverWait
from base_html.webdriver.support.ec.fabric import ECFabric

base_webdriver = Type[BaseWebDriverFabric.REMOTE_WEB_DRIVER_SELENIUM]


class TextToBePresentInElement(ICheckText):
    """TextToBePresentInElement class."""

    def __init__(self,
                 driver: base_webdriver,
                 locator: Tuple[str, str],
                 text: str,
                 time: float = 10):
        """Initialize."""
        self.__driver = driver
        self.__locator = locator
        self.__text = text
        self.__time = time

    def check_text(self) -> bool:
        """Check if the given text matches the text on the given webelement."""
        return WebDriverWait.WDW_SELENIUM(self.__driver, self.__time).until(
            ECFabric.EC_SELENIUM.text_to_be_present_in_element(self.__locator,
                                                               self.__text),
            message=f"Can't find elements by locator {self.__locator}")
