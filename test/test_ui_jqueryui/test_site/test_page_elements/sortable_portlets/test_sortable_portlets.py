"""Test sortable portlets."""

from page_object.page_elements.sortable_portlets import (
    SortablePortlets, AllPlayLoads)


def test_sortable_portlets(wd):
    """Check if an additional menu is displayed."""
    page = SortablePortlets(wd)
    page.get_page("https://jqueryui.com/sortable/#portlets")
    page.switch_frame(page.IFRAME)
    first_cells = page.find_elements(page.COLUMNS, page.CELLS)
    source_elmt = first_cells[0]
    destination_elmt = first_cells[1]

    AllPlayLoads.STANDART(page.driver, source_elmt, page.get_offset(
        source_elmt, destination_elmt)).run()

    second_cells = page.find_elements(page.COLUMNS, page.CELLS)

    assert first_cells != second_cells
