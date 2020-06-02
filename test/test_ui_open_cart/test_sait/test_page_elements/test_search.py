"""Test search element."""

from page_object.page_elements.search import SearchElmnt


def test_search_element(wd):
    """Test transition to the search result page from the search form."""
    search_elmt = SearchElmnt(wd)
    search_elmt.get_page("http://demo-opencart.ru/index.php")
    search_elmt.enter_word("Hello")
    search_elmt.click_on_the_search_button_cascade()

    assert "route=product/search" in search_elmt.get_current_url
