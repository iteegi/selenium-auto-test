"""Selenium webdriver."""

from selenium import webdriver


def __get_chrome_wd(*args, **kwargs):
    return webdriver.Chrome(*args, **kwargs)
