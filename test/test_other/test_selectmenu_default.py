import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_selectmenu_default(wd):

    wd.get("https://jqueryui.com/selectmenu/")

    wait = WebDriverWait(wd, 5)

    frm = wait.until(
        es.presence_of_all_elements_located((By.TAG_NAME, 'iframe')))
    wd.switch_to.frame(frm[0])

    elmt = wd.find_element_by_xpath("//select[@name='speed']")
    print(elmt.tag_name)

    s = Select(elmt)
    for d in s.options:
        print(d.get_attribute("textContent"))
    wd.execute_script('$( "#speed" ).selectmenu( "open" );')

    el = wd.find_elements_by_tag_name(
        "body > div.ui-selectmenu-menu.ui-front.ui-selectmenu-open")

    assert el[0].is_displayed()

    wd.switch_to.default_content()
