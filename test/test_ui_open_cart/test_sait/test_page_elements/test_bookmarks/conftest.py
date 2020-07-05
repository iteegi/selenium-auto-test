"""Conftest."""

import pytest
import time

from base_html.webdriver import WebDriver, Options


@pytest.fixture(scope="session")
def start():
    """Web driver creation fixture."""
    o = Options.Options_SELENIUM()
    o.add_argument("start-maximized")
    wd = WebDriver.CHROME_SELENIUM(options=o)
    yield wd
    time.sleep(3)
    wd.quit()


@pytest.fixture(scope="function")
def wd(start):
    """Clear your cookies before each test."""
    yield start
    start.delete_all_cookies()
