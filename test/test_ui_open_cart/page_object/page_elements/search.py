"""Search page object."""

from base_html.html.base import HTMLPage
from base_html.webdriver.common.by import ByFabric
from base_html.webdriver.common.keys import Keys


class SearchElmnt(HTMLPage):
    """SearchElmnt class."""

    SEARCH_FIELD = (ByFabric.by(ByFabric.OS.BY).NAME, "search")
    SEARCH_TARGET = (ByFabric.by(ByFabric.OS.BY).ID, "search")
    SEARCH_BUTTON = (ByFabric.by(ByFabric.OS.BY).TAG_NAME, "button")

    def enter_word(self, word):
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
