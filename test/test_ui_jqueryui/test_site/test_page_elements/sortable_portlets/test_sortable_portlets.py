"""Test sortable portlets."""

from page_object.page_elements.sortable_portlets import SortablePortlets


def test_sortable_portlets(wd):
    """Check if an additional menu is displayed."""
    page = SortablePortlets(wd)
    page.get_page("https://jqueryui.com/sortable/#portlets")

    print(len(page.find_all_cells()))
