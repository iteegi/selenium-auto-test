"""Test select menu default."""

# from test import test_ui_jqueryui
from page_object.page_elements.select_menu import SelectMenuDefault


def test_select_menu_default(wd):
    """Check if an additional menu is displayed."""
    page = SelectMenuDefault(wd)
    page.get_page("https://jqueryui.com/selectmenu/")
