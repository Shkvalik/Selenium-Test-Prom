from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def should_be_correct_name_category(self):
        assert MainPageLocators.PART_NAME_CATEGORY_URL in self.browser.current_url, f"Current url is incorrect --> {self.browser.current_url}"

    def add_goods_to_favorites(self):
        button = self.browser.find_element(*MainPageLocators.BUTTON_ADD_TO_FAVORITES)
        button.click()

    def remove_goods_from_favorites(self):
        button = self.browser.find_element(*MainPageLocators.BUTTON_ADD_TO_FAVORITES)
        button.click()

