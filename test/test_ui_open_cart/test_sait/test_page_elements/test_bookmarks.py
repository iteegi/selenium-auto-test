"""Test bookmarks."""

from page_object.page_elements.bookmarks import BookmarksElmnt


def test_wishlist(wd):
    """Test for correct text change in the wishlist."""
    search_elmt = BookmarksElmnt(wd)
    search_elmt.get_page("http://demo-opencart.ru/index.php")
    assert search_elmt.check_wishlist()
