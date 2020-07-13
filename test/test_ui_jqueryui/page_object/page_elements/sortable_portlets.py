"""Page object for sortable portlets."""
from typing import Type, Tuple, List
from abc import ABC, abstractmethod

from base_html.html.base import HTMLPage
from base_html.webdriver.common.by import By
from base_html.webdriver.common.action_chains import ActionChains
from base_html.webdriver.support.wait.fabric import WebDriverWait
from base_html.webdriver.remote.webdriver.fabric import BaseWebDriverFabric
from base_html.webdriver.remote.webelement.fabric import BaseWebElementFabric
from base_html.webdriver.support.ec.fabric import ECFabric
from patterns.generating.factory_method import FactoryMethod

base_webdriver = Type[BaseWebDriverFabric.REMOTE_WEB_DRIVER_SELENIUM]
base_webelement = Type[BaseWebElementFabric.REMOTE_WEB_ELEMENT_SELENIUM]


class IPlayLoad(ABC):
    """Interface for playLoad."""

    @abstractmethod
    def run(self) -> None:
        """Run action."""
        pass


class StandartPlayLoad(IPlayLoad):
    """Standart playLoad."""

    def __init__(self,
                 driver: base_webdriver,
                 source: base_webelement,
                 offset: Tuple[float, float]) -> None:
        """Initialize."""
        self.__driver = driver
        self.__source = source
        self.__offset = offset

    def run(self) -> None:
        """Run action."""
        act = ActionChains.ACTIONCHAINS_SELENIUM(self.__driver)
        act.move_to_element(self.__source)
        act.click_and_hold()
        act.move_by_offset(*self.__offset)
        act.perform()
        act.release()
        act.reset_actions()


@FactoryMethod
class AllPlayLoads():
    """Factory Method for playloads."""

    STANDART = StandartPlayLoad


class SortablePortlets(HTMLPage):
    """Class describing sortable portlets page."""

    IFRAME = (By.BY_SELENIUM.TAG_NAME, "iframe")
    COLUMNS = (By.BY_SELENIUM.CSS_SELECTOR, "div.ui-sortable")
    CELLS = (By.BY_SELENIUM.CSS_SELECTOR, "div.portlet-header")

    def get_offset(self,
                   source: base_webelement,
                   destination: base_webelement) -> Tuple[float, float]:
        """Calculate element offset."""
        return (0, 1.5 * destination.location['y']
                - source.location['y'])

    def find_elements(self,
                      target: Tuple[str, str],
                      locator: Tuple[str, str]) -> List[base_webelement]:
        """Find all elements in the first cell of the element matrix."""
        return self.find_elmnts_cascade(target, locator)

    def switch_frame(self,
                     frame: Tuple[str, str],
                     time: float = 10) -> None:
        """Switch to a given frame."""
        frm = self.find_elmnt(frame, time)

        WebDriverWait.WDW_SELENIUM(
            self.driver, time).until(
                ECFabric.SCROLL_TO_ELEMENT(frm))

        self.switch_to_frame(frm)
