"""Test select menu default."""

from page_object.page_elements.select_menu import SelectMenuDefault


def test_select_menu_default(wd):
    """Check if an additional menu is displayed."""
    page = SelectMenuDefault(wd)
    page.get_page("https://jqueryui.com/selectmenu/")
    el = page.execute_script_and_return_item(
        '$( "#speed" ).selectmenu( "open" );')
    assert el.is_displayed()
