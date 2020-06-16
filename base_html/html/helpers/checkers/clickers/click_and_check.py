"""Clickers."""

from typing import Type

from . interfaces.iclick import IClick
from base_html.html.helpers.iterators.interfaces.iiter import IIterator
from base_html.html.helpers.comparators.check_text.interfaces.icheckertext import ICheckText

from base_html.webdriver.support.wait import WebDriverWait
from base_html.webdriver.support.ec.interfaces.iec import IExpectedConditions
from base_html.webdriver.remote.webdriver.fabric import BaseWebDriverFabric
from base_html.common.exception.fabric import ExceptionFabric

base_webdriver = Type[BaseWebDriverFabric.REMOTE_WEB_DRIVER_SELENIUM]
extion = ExceptionFabric.EXCEPTIONS_SELENIUM.ElementClickInterceptedException


class ClickAndCheck(IClick):
    """Click on an element and check the parameter of another element.

    Click on an element and check the changed parameter value
    of another element.
    """

    def __init__(self,
                 driver: base_webdriver,
                 ec: Type[IExpectedConditions],
                 iter_func: Type[IIterator],
                 matcher_func: Type[ICheckText]) -> None:
        """Initialize."""
        self.__driver = driver
        self.__ec = ec
        self.__iter_func = iter_func
        self.__matcher_func = matcher_func

    def run(self, time: float = 10) -> bool:
        """Start checking the value of an element.

        Click on each element of a given sequence and check
        whether the parameter of the control element has changed correctly.
        """
        for i in self.__iter_func.get_item():
            WebDriverWait.WDW_SELENIUM(self.__driver, time)\
                .until(self.__ec)
            while True:
                try:
                    i.click()
                except extion:
                    continue
                else:
                    break
        return self.__matcher_func.check_text()
