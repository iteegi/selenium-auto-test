"""Test bookmarks."""

import pytest
from page_object.page_elements.bookmarks import BookmarksElmnt


# TODO: исправить scope для фикстуры. для каждого параметра новый браузер.
@pytest.mark.parametrize('f', [1, 2, 0])
def test_wishlist(wd, f):
    """Test for correct text change in the wishlist."""
    search_elmt = BookmarksElmnt(wd)
    search_elmt.get_page("http://demo-opencart.ru/index.php")
    assert search_elmt.check_wishlist(quantity=f)
