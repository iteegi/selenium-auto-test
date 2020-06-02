from selenium.webdriver.common.action_chains import ActionChains


def test_sortable_portlets(wd):

    wd.get("https://jqueryui.com/sortable/#portlets")

    wd.switch_to.frame(wd.find_elements_by_tag_name('iframe')[0])
    elmts = wd.find_elements_by_css_selector(
        "div.portlet-header.ui-sortable-handle.ui-widget-header.ui-corner-all")

    source_elmt = elmts[0]
    destination_elmt = elmts[1]

    act = ActionChains(wd)
    act.move_to_element(source_elmt)
    act.click_and_hold()

    act.move_by_offset(0,
                       1.5 * destination_elmt.location['y']
                       - source_elmt.location['y'])

    act.perform()

    act.release()
    act.perform()

    wd.switch_to.default_content()

    elmts2 = wd.find_elements_by_css_selector(
        "div.portlet-header.ui-sortable-handle.ui-widget-header.ui-corner-all")

    assert elmts != elmts2
