# File for configuration tests in project(pytest)
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()
