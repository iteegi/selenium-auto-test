"""Conftest."""

import pytest
import time

from base_html.webdriver import WebDriver, Options


@pytest.fixture(scope="session")
def wd() -> None:
    """Web driver creation fixture."""
    o = Options.Options_SELENIUM()
    o.add_argument("start-maximized")
    wd = WebDriver.CHROME_SELENIUM(options=o)
    yield wd
    time.sleep(3)
    wd.quit()
