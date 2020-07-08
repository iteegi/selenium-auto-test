"""Page object for sortable portlets."""

from base_html.html.base import HTMLPage
from base_html.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time as t


class SortablePortlets(HTMLPage):

    IFRAME = (By.BY_SELENIUM.TAG_NAME, "iframe")
    COLUMNS = (By.BY_SELENIUM.CSS_SELECTOR, "div.ui-sortable")
    CELLS = (By.BY_SELENIUM.XPATH, ".//*")

    def find_all_cells(self, time=10):
        frm = self.find_elmnt(self.IFRAME, time)
        print(f"_____ {frm.location['y']}")
        a = self.driver.execute_script("arguments[0].scrollIntoView(true);return window.pageYOffset",
                                   frm)

        print(f"-------{a}--------")
        self.switch_to_frame(frm)
        all_columns = self.find_elmnts(self.COLUMNS, time)
        print(f"---->{len(all_columns)}")
        all_cells = []

        for i in range(len(all_columns)):
            # print(f">>>---{i} ==== {len(all_columns[i])}")

            # TODO: может через cascade
            j = all_columns[i].find_elements(By.BY_SELENIUM.CSS_SELECTOR, "div.portlet-header")

            # print(f"---{i} ==== {len(j)}")
            for k in range(len(j)):
                # print(f"====> {type(j[k])}")
                # fo = j[k].get_attribute('class')
                # print(f"====> {fo}")
                all_cells.append(j[k])

        print("================")
        for i in range(len(all_cells)):
            print(all_cells[i])
        print("================")

        lx = self.find_elmnts_cascade(self.COLUMNS, (By.BY_SELENIUM.CSS_SELECTOR, "div.portlet-header"))
        print("================")
        for i in range(len(lx)):
            print(lx[i])
        print("================")

        source_elmt = all_cells[0]
        destination_elmt = all_cells[1]

        print(f"==== {source_elmt.text} ====")
        print(f"==== {destination_elmt.text} ====")

        # t.sleep(3)

        act = ActionChains(self.driver)
        act.move_to_element(source_elmt)
        act.click_and_hold()

        act.move_by_offset(0,
                           1.5 * destination_elmt.location['y']
                           - source_elmt.location['y'])

        act.perform()
        # t.sleep(5)

        act.release()
        act.reset_actions()
        # act.perform()


        lx2 = self.find_elmnts_cascade(self.COLUMNS, (By.BY_SELENIUM.CSS_SELECTOR, "div.portlet-header"))
        print("================")
        for i in range(len(lx2)):
            print(lx2[i])
        print("================")

        # assert lx2 == lx
        # return [lx, lx2]
        # return 0
        return all_cells
