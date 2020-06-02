"""webdriver."""

from base_html.webdriver.support.wait import web_driver_wait
from base_html.webdriver.support.expected_conditions import get_EC as EC
from base_html.html.different_functions.dif_func import exec_func_several_times


class HTMLPage:
    """Web page."""

    def __init__(self, driver):
        """Object initialization."""
        self.driver = driver

    def find_elmnt(self, locator, time=10):
        """Find element."""
        return web_driver_wait(self.driver, time).until(
            EC().presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}")

    def find_elmnt_cascade(self, target, locator, time=10):
        """Find element by cascade method."""
        trgt = web_driver_wait(self.driver, time).until(
            EC().presence_of_element_located(target),
            message=f"Can't find element by locator {locator}")
        return trgt.find_element(*locator)

    def find_elmnts(self, locator, time=10):
        """Fond elements."""
        return web_driver_wait(self.driver, time).until(
            EC().presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}")

    def find_elmnts_cascade(self, target, locator, time=10):
        """Find elements by cascade method."""
        trgt = web_driver_wait(self.driver, time).until(
            EC().presence_of_elements_located(target),
            message=f"Can't find element by locator {locator}")
        return trgt.find_elements(*locator)

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

    def click_and_check_text(self, locator, text_element,
                             text, quantity=1, time=10):
        """Click on the button and check text.

        Click on the button and check if the text
        on the other element matches the specified.
        """
        self.click_on_the_button(locator, quantity, time=1)
        return self.check_text_matches(text_element, text)

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
            search_field.send_keys(word+key)
        return search_field

    def get_page(self, url):
        """Get web pasge."""
        self.driver.get(url)

    @property
    def get_current_url(self):
        """Get current url."""
        return self.driver.current_url
