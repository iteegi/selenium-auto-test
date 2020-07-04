"""Bookmarks page object."""

from base_html.html.base import HTMLPage
from base_html.webdriver.common.by import By
from base_html.helpers.checkers.clickers.click_and_check import (
    ClickAndCheck)
from base_html.webdriver.support.ec.fabric import ECFabric
from base_html.helpers.iterators.get_element import OneElementOutOfMany
from base_html.helpers.comparators.check_text.check_text import (
    TextToBePresentInElement as Checker)


class BookmarksElmnt(HTMLPage):
    """BookmarksElmnt class."""

    INVESTIGATING_TEXT_ELEMENT = (By.BY_SELENIUM.XPATH,
                                  "//a[@id='wishlist-total']")

    CONTROL_BUTTON = (By.BY_SELENIUM.XPATH,
                      "//*[@data-original-title='В закладки']")

    def check_wishlist(self,
                       quantity: int = 1,
                       time: float = 10) -> bool:
        """To check whether the changed text on a web element.

        quantity = 0 is the value of all.
        """
        if quantity == 0:
            text = "Закладки ({0})".format(self.__get_text(time))
        else:
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

    def __get_text(self, time=10):
        items = self.find_elmnts(self.CONTROL_BUTTON, time)
        return len(items)
