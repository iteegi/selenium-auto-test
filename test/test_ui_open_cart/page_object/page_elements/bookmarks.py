"""Bookmarks page object."""

from base_html.html.base import HTMLPage
from base_html.webdriver.common.by import ByFabric
from base_html.html.helpers.checkers.clickers.click_and_check import (
    ClickAndCheck)
from base_html.webdriver.support.ec.fabric import ECFabric
from base_html.html.helpers.iterators.get_element import OneElementOutOfMany
from base_html.html.helpers.comparators.check_text.check_text import (
    TextToBePresentInElement as Checker)


class BookmarksElmnt(HTMLPage):
    """BookmarksElmnt class."""

    INVESTIGATING_TEXT_ELEMENT = (ByFabric.by(ByFabric.OS.BY).XPATH,
                                  "//a[@id='wishlist-total']")

    CONTROL_BUTTON = (
        ByFabric.by(ByFabric.OS.BY).XPATH,
        "//*[@data-original-title='В закладки']")

    def check_wishlist(self, quantity=1, time=10):
        text = "Закладки ({0})".format(quantity)
        check = ClickAndCheck(self.driver,
                              ECFabric.EXEC_SCRIPT_RETURN_ZERO(
                                  "return window.pageYOffset"),
                              OneElementOutOfMany(
                                  self.driver,
                                  self.CONTROL_BUTTON,
                                  quantity,
                                  time),
                              Checker(self.driver,
                                      self.INVESTIGATING_TEXT_ELEMENT,
                                      text, time))
        return check.run()
