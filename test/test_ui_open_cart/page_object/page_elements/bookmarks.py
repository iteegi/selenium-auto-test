"""Bookmarks page object."""

from base_html.html.base import HTMLPage
from base_html.webdriver.common.by import ByFabric
from base_html.html.helpers.checkers.clickers import ClickAndCheck
from base_html.webdriver.support.ec.fabric import ECFabric
from base_html.html.helpers.iterators.get_element import F
from base_html.html.helpers.comparators.check_text import Checker


class BookmarksElmnt(HTMLPage):
    """SearchElmnt class."""

    CONTROL_BUTTON = (
        ByFabric.by(ByFabric.OS.BY).XPATH,
        "//*[@id='content']/div[2]/div[1]/div/div[3]/button[2]")
    INVESTIGATING_TEXT_ELEMENT = (ByFabric.by(ByFabric.OS.BY).XPATH,
                                  "//a[@id='wishlist-total']")

    CONTROL_BUTTON_2 = (
        ByFabric.by(ByFabric.OS.BY).XPATH,
        "//*[@data-original-title='В закладки']")

    def check_wishlist(self, quantity=1, time=10):
        text = "Закладки ({0})".format(quantity)
        # h = ECFabric.ec(ECFabric.Choice.EX, "jyfggy")
        # print("----{}".format(h))
        check = ClickAndCheck(self.driver,
                              ECFabric.ec(ECFabric.Choice.EX)(
                                  "return window.pageYOffset"),
                              F(self.driver, self.CONTROL_BUTTON_2,
                                quantity, time),
                              Checker(self.driver,
                                      self.INVESTIGATING_TEXT_ELEMENT,
                                      text, time))
        return check.run()
















    def check_wishlist2(self, quantity=1, time=10):
        """Check if the text in the wish list has changed correctly."""
        text = "Закладки ({0})".format(quantity)

        # return self.click_and_check_text(self.CONTROL_BUTTON_2,
        #                                  self.INVESTIGATING_TEXT_ELEMENT,
        #                                  text,
        #                                  quantity)

        self.click_and_check_text(self.CONTROL_BUTTON_2, quantity, time)
        return self.check_text_matches(self.INVESTIGATING_TEXT_ELEMENT,
                                       text, time)
