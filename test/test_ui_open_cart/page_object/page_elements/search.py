"""Search page object."""

from typing import Type

from base_html.html.base import HTMLPage
from base_html.webdriver.common.by import By
from base_html.webdriver.common.keys import Keys
from base_html.webdriver.remote.webelement.fabric import BaseWebElementFabric

base_webelement = Type[BaseWebElementFabric.REMOTE_WEB_ELEMENT_SELENIUM]


class SearchElmnt(HTMLPage):
    """SearchElmnt class."""

    SEARCH_FIELD = (By.BY_SELENIUM.NAME, "search")
    SEARCH_TARGET = (By.BY_SELENIUM.ID, "search")
    SEARCH_BUTTON = (By.BY_SELENIUM.TAG_NAME, "button")

    def enter_word(self, word: str) -> base_webelement:
        """Enter a phrase in the search bar."""
        return self.insert_phrase(self.SEARCH_FIELD,
                                  word,
                                  Keys.KEYS_SELENIUM.BACKSPACE,
                                  time=1)

    def click_on_the_search_button_cascade(self,
                                           quantity: int = 1,
                                           time: float = 1) -> None:
        """Find the button in the item tree and click it."""
        self.click_on_the_button_cascade(
            self.SEARCH_TARGET, self.SEARCH_BUTTON, quantity, time)
