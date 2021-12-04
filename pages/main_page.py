from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def should_be_correct_name_category(self):
        assert MainPageLocators.NAME_CATEGORY in self.browser.current_url, f"Current url is incorrect --> {self.browser.current_url}"

    def add_good_to_favorites(self):
        button = self.browser.find_element(*MainPageLocators.BUTTON_ADD_TO_FAVORITE)
        button.click()