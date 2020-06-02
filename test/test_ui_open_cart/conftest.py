"""Conftest."""

import pytest
from base_html.webdriver.chrome.webdriver import chrome
from base_html.webdriver.chrome.options import options
import time


@pytest.fixture(scope="session")
def wd():
    """Web driver creation fixture."""
    o = options()
    o.add_argument("start-maximized")
    wd = chrome(options=o)
    yield wd
    time.sleep(3)
    wd.quit()
