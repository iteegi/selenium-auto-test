"""Page object for select menu."""

from base_html.html.base import HTMLPage
from base_html.webdriver.common.by import By


class SelectMenuDefault(HTMLPage):
    """Class describing selectmenu for standard functionality."""

    IFRAME = (By.BY_SELENIUM.TAG_NAME, "iframe")
    SELECTMENU = (By.BY_SELENIUM.CLASS_NAME, "ui-selectmenu-open")

    def switch_to_frame(self, time=10):
        frm = self.find_elmnt(self.IFRAME, time)
        self.driver.switch_to.frame(frm)
