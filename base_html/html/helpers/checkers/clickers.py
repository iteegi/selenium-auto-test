"""Clickers."""

from base_html.webdriver.support.wait import web_driver_wait
from selenium.common.exceptions import ElementClickInterceptedException


class ClickAndCheck():
    """Click on an element and check the parameter of another element.

    Click on an element and check the changed parameter value
    of another element.
    """

    def __init__(self, driver, ec, iter_func, matcher_func):
        """Initialize."""
        self.__driver = driver
        self.__ec = ec
        self.__iter_func = iter_func
        self.__matcher_func = matcher_func

    def run(self, time=10):
        """Start checking the value of an element.

        Click on each element of a given sequence and check
        whether the parameter of the control element has changed correctly.
        """
        for i in self.__iter_func.get_item():
            web_driver_wait(self.__driver, time)\
                .until(self.__ec)
            while True:
                try:
                    i.click()
                except ElementClickInterceptedException:
                    continue
                else:
                    break
        return self.__matcher_func.check_text()
