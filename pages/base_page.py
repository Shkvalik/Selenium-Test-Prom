from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LOGIN_DATA import EMAIL, PASSWORD
from pages.locators import MainPageLocators, BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def login(self):
        button_login = self.browser.find_element(*BasePageLocators.BUTTON_LOGIN)
        button_login.click()
        button_login_by_email = self.browser.find_element(*BasePageLocators.BUTTON_LOGIN_BY_EMAIL)
        button_login_by_email.click()
        input_email = self.browser.find_element(*BasePageLocators.INPUT_LOGIN)
        input_email.send_keys(EMAIL)
        button_confirm_email = self.browser.find_element(*BasePageLocators.BUTTON_CONFIRM_INPUT_LOGIN)
        button_confirm_email.click()
        input_password = self.browser.find_element(*BasePageLocators.INPUT_PASSWORD)
        input_password.send_keys(PASSWORD)
        button_confirm_password = self.browser.find_element(*BasePageLocators.BUTTON_CONFIRM_INPUT_PASSWORD)
        button_confirm_password.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.BUTTON_CABINET), "User is not authorized on the site"

    def must_be_counter_favorites_goods(self):
        assert self.is_element_present(*BasePageLocators.COUNTER_FAVORITES_GOODS), "Counter isn't display"

    def musnt_be_counter_favorites_goods(self):
        assert self.is_not_element_present(*BasePageLocators.COUNTER_FAVORITES_GOODS,
                                           timeout=2), "Counter isn't display"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def go_to_favorites_page(self):
        button = self.browser.find_element(*BasePageLocators.BUTTON_FAVORITES)
        button.click()
