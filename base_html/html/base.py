"""webdriver."""

from typing import Type, Tuple, List

from base_html.webdriver.support.wait import web_driver_wait
from base_html.webdriver.support.expected_conditions import get_EC as EC
from base_html.html.different_functions.dif_func import exec_func_several_times

from selenium.common.exceptions import ElementNotVisibleException
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
import time as t

from base_html.webdriver.common.by import ByFabric

from base_html.webdriver.remote.webdriver.fabric import BaseWebDriverFabric
from base_html.webdriver.remote.webelement.fabric import BaseWebElementFabric
from base_html.webdriver.support.wait.fabric import WebDriverWait
from base_html.webdriver.support.ec.fabric import ECFabric

base_webdriver = Type[BaseWebDriverFabric.REMOTE_WEB_DRIVER_SELENIUM]
base_webelement = Type[BaseWebElementFabric.REMOTE_WEB_ELEMENT_SELENIUM]


class HTMLPage:
    """Web page."""

    def __init__(self, driver: base_webdriver) -> None:
        """Object initialization."""
        self.driver = driver

    def find_elmnt(self,
                   locator: Tuple[str, str],
                   time: float = 10) -> base_webelement:
        """Find element."""
        return WebDriverWait.WDW_SELENIUM(self.driver, time).until(
            ECFabric.EC_SELENIUM.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}")

    def find_elmnt_cascade(self,
                           target: Tuple[str, str],
                           locator: Tuple[str, str],
                           time: float = 10) -> base_webelement:
        """Find element by cascade method.

        target - selector where you want to find another element
        locator - element selector

        """
        return WebDriverWait.WDW_SELENIUM(self.driver, time).until(
            ECFabric.ELEMENT_LOCATED_CASCADE(target, locator),
            message=f"Can't find element by target {target} or\
                locator {locator}")

    def find_elmnts(self,
                    locator: Tuple[str, str],
                    time: float = 10) -> List[base_webelement]:
        """Find elements."""
        return WebDriverWait.WDW_SELENIUM(self.driver, time).until(
            ECFabric.EC_SELENIUM.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}")

    def find_elmnts_cascade(self,
                            target: Tuple[str, str],
                            locator: Tuple[str, str],
                            time: float = 10) -> List[base_webelement]:
        """Find elements by cascade method.

        target - selector where you want to find another elements
        locator - elements selector

        """
        return WebDriverWait.WDW_SELENIUM(self.driver, time).until(
            ECFabric.ELEMENTS_LOCATED_CASCADE(target),
            message=f"Can't find element by target {target} or\
                locator {locator}")

    def click_on_the_button_cascade(self, target, locator,
                                    quantity=1,
                                    time=10):
        """Find the button and click on it by cascade method."""
        elmt = self.find_elmnt_cascade(target, locator, time)
        exec_func_several_times(elmt.click, quantity)

    def click_on_the_button(self, locator, quantity=1, time=10):
        """Find the button and click on it."""
        elmt = self.find_elmnt(locator, time)
        exec_func_several_times(elmt.click, quantity)

    def check_text_matches(self, text_element, text, time=10):
        """Check if the text matches."""
        return web_driver_wait(self.driver, time).until(
            EC().text_to_be_present_in_element(text_element, text),
            message=f"Can't find elements by locator {text_element}")

    def insert_phrase(self, locator, word, key=None, time=10):
        """Insert a phrase into a given web element."""
        search_field = self.find_elmnt(locator, time)
        if key is None:
            search_field.send_keys(word)
        else:
            search_field.send_keys(word + key)
        return search_field

    def get_page(self, url):
        """Get web pasge."""
        self.driver.get(url)

    @property
    def get_current_url(self):
        """Get current url."""
        return self.driver.current_url
