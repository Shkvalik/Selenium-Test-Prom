from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def should_be_correct_name_category(self):
        name_category = self.browser.find_element(*MainPageLocators.NAME_CATEGORY).text
        assert name_category == 'Велосипедные шины', self.browser.current_url
