"""Custom iterators."""

from typing import Tuple, Iterator, List

from base_html.webdriver.support.wait import WebDriverWait
from base_html.webdriver.support.ec.fabric import ECFabric

# TODO: избавиться от селениума
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class OneElementOutOfMany():
    """Returns each item found in turn."""

    def __init__(self,
                 driver: WebDriver,
                 locators: Tuple[str, str],
                 quantity: int = 1,
                 time: int = 10) -> None:
        """Initialize.

        quantity = 0 is equivalent to getting all items
        """
        self.__driver = driver
        self.__locators = locators
        self.__quantity = quantity
        self.__time = time

    def get_item(self) -> Iterator[WebElement]:
        """Get all found items one at a time."""
        elm = WebDriverWait.WDW_SELENIUM(self.__driver, self.__time).until(
            ECFabric.EC_SELENIUM.presence_of_all_elements_located(
                self.__locators)
            )
        quantity_elemts = len(elm)

        if self.__quantity == 0:
            return self.__item_iter(elm, quantity_elemts)
        else:
            return self.__item_iter(elm, self.__quantity)

    def __item_iter(self,
                    elements: List[WebElement],
                    quantity: int) -> Iterator[WebElement]:
        """Return element iterator."""
        for i in range(quantity):
            yield elements[i]
