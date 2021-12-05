import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.set_window_size(1600, 800)
    yield browser
    print("\nquit browser..")
    browser.quit()