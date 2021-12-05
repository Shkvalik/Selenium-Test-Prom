from pages.base_page import BasePage
from pages.locators import GoodsPageLocators


class GoodsPage(BasePage):
    def heart_is_filled_with_color(self):
        heart = self.browser.find_element(*GoodsPageLocators.HEART).get_attribute('d')
        assert 'M10' in heart

    def heart_is_not_filled_with_color(self):
        heart = self.browser.find_element(*GoodsPageLocators.HEART).get_attribute('d')
        assert 'M14.5' in heart

    def must_be_correct_name_category(self):
        assert GoodsPageLocators.PART_GOODS_NAME_URL in self.browser.current_url, f"Current url is incorrect --> {self.browser.current_url}"

    def add_goods_to_favorites(self):
        button = self.browser.find_element(*GoodsPageLocators.BUTTON_ADD_TO_FAVORITES)
        button.click()
