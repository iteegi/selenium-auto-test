"""Page object for sortable portlets."""

from base_html.html.base import HTMLPage
from base_html.webdriver.common.by import By


class SortablePortlets(HTMLPage):

    IFRAME = (By.BY_SELENIUM.TAG_NAME, "iframe")
    COLUMNS = (By.BY_SELENIUM.CSS_SELECTOR, "div.ui-sortable")
    CELLS = (By.BY_SELENIUM.XPATH, ".//*")

    def find_all_cells(self, time=10):
        all_columns = self.find_elmnts(self.COLUMNS, time)
        all_cells = []

        for i in range(len(all_columns)):
            all_cells.append(all_columns[i].find_elmnts(self.CELLS, time))

        return all_cells
