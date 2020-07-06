"""Page object for select menu."""

from typing import Type

from base_html.html.base import HTMLPage
from base_html.webdriver.common.by import By
from base_html.webdriver.remote.webelement.fabric import BaseWebElementFabric

base_webelement = Type[BaseWebElementFabric.REMOTE_WEB_ELEMENT_SELENIUM]


class SelectMenuDefault(HTMLPage):
    """Class describing selectmenu for standard functionality."""

    IFRAME = (By.BY_SELENIUM.TAG_NAME, "iframe")
    SELECTMENU = (By.BY_SELENIUM.CLASS_NAME, "ui-selectmenu-open")

    def execute_script_and_return_item(self,
                                       script: str,
                                       time: float = 10) -> base_webelement:
        """Execute the script and find the item that appears."""
        frm = self.find_elmnt(self.IFRAME, time)
        self.switch_to_frame(frm)
        self.exec_script(script)
        return self.find_elmnt(self.SELECTMENU, time)
