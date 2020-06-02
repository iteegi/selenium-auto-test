import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


@pytest.fixture(scope="session")
def wd():
    wd = webdriver.Chrome()
    yield wd
    time.sleep(5)
    wd.quit()
