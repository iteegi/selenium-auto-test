"""Bookmarks page object."""

from base_html.html.base import HTMLPage
from base_html.webdriver.common.by import ByFabric


class BookmarksElmnt(HTMLPage):
    """SearchElmnt class."""

    CONTROL_BUTTON = (
        ByFabric.by(ByFabric.OS.BY).XPATH,
        "//*[@id='content']/div[2]/div[1]/div/div[3]/button[2]")
    INVESTIGATING_TEXT_ELEMENT = (ByFabric.by(ByFabric.OS.BY).XPATH,
                                  "//a[@id='wishlist-total']")

    def check_wishlist(self, quantity=1):
        """Check if the text in the wish list has changed correctly."""
        text = "Закладки ({0})".format(quantity)
        return self.click_and_check_text(self.CONTROL_BUTTON,
                                         self.INVESTIGATING_TEXT_ELEMENT,
                                         text,
                                         quantity)
