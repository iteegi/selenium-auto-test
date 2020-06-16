"""TextToBePresentInElement."""

from base_html.webdriver.support.wait import web_driver_wait
from base_html.webdriver.support.expected_conditions import get_EC as EC


class TextToBePresentInElement():
    """TextToBePresentInElement class."""

    def __init__(self, driver, text_element, text, time=10):
        self.__driver = driver
        self.__text_element = text_element
        self.__text = text
        self.__time = time

    def check_text(self):
        """Check if the text matches."""
        return web_driver_wait(self.__driver, self.__time).until(
            EC().text_to_be_present_in_element(self.__text_element,
                                               self.__text),
            message=f"Can't find elements by locator {self.__text_element}")
