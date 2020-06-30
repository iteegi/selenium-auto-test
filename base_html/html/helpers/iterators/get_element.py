"""Custom iterators."""

from typing import Tuple, Type, Iterator, List

from base_html.html.helpers.iterators.interfaces.iiter import IIterator

from base_html.webdriver.support.wait.fabric import WebDriverWait
from base_html.webdriver.support.ec.fabric import ECFabric
from base_html.webdriver.remote.webdriver.fabric import BaseWebDriverFabric
from base_html.webdriver.remote.webelement.fabric import BaseWebElementFabric

base_webdriver = Type[BaseWebDriverFabric.REMOTE_WEB_DRIVER_SELENIUM]
base_webelement = Type[BaseWebElementFabric.REMOTE_WEB_ELEMENT_SELENIUM]


class OneElementOutOfMany(IIterator):
    """Returns each item found in turn."""

    def __init__(self,
                 driver: base_webdriver,
                 locators: Tuple[str, str],
                 quantity: int = 1,
                 time: float = 10) -> None:
        """Initialize.

        quantity = 0 is equivalent to getting all items
        """
        self.__driver = driver
        self.__locators = locators
        self.__quantity = quantity
        self.__time = time

    def get_item(self) -> base_webelement:
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
                    elements: List[base_webelement],
                    quantity: int) -> Iterator[base_webelement]:
        """Return element iterator."""
        for i in range(quantity):
            yield elements[i]
