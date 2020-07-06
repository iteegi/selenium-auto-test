"""Conftest."""

import pytest
import time
from typing import Iterator, Type

from base_html.webdriver import WebDriver, Options
from base_html.webdriver.remote.webdriver.fabric import BaseWebDriverFabric

base_webdriver = Type[BaseWebDriverFabric.REMOTE_WEB_DRIVER_SELENIUM]


@pytest.fixture(scope="session")
def wd() -> Iterator[base_webdriver]:
    """Web driver creation fixture."""
    o = Options.Options_SELENIUM()
    o.add_argument("start-maximized")
    wd = WebDriver.CHROME_SELENIUM(options=o)
    yield wd
    time.sleep(3)
    wd.quit()
