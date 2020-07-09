"""Page object for sortable portlets."""

from base_html.html.base import HTMLPage
from base_html.webdriver.common.by import By
from base_html.webdriver.common.action_chains import ActionChains
from base_html.webdriver.support.wait.fabric import WebDriverWait
from base_html.webdriver.support.ec.fabric import ECFabric


class SortablePortlets(HTMLPage):

    IFRAME = (By.BY_SELENIUM.TAG_NAME, "iframe")
    COLUMNS = (By.BY_SELENIUM.CSS_SELECTOR, "div.ui-sortable")
    CELLS = (By.BY_SELENIUM.CSS_SELECTOR, "div.portlet-header")

    def find_all_cells(self, time=10):
        """Return a list of items before and after the action."""
        frm = self.find_elmnt(self.IFRAME, time)

        WebDriverWait.WDW_SELENIUM(
            self.driver, time).until(
                ECFabric.SCROLL_TO_ELEMENT(frm))

        self.switch_to_frame(frm)

        first_cells = self.find_elmnts_cascade(self.COLUMNS, self.CELLS)

        source_elmt = first_cells[0]
        destination_elmt = first_cells[1]

        act = ActionChains.ACTIONCHAINS_SELENIUM(self.driver)
        act.move_to_element(source_elmt)
        act.click_and_hold()

        act.move_by_offset(0,
                           1.5 * destination_elmt.location['y']
                           - source_elmt.location['y'])

        act.perform()

        act.release()
        act.reset_actions()

        second_cells = self.find_elmnts_cascade(self.COLUMNS, self.CELLS)

        return [first_cells, second_cells]
