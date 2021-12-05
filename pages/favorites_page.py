from .base_page import BasePage
from .locators import FavoritesPageLocators


class FavoritesPage(BasePage):
    def favorites_must_be_empty(self):
        assert self.is_not_element_present(*FavoritesPageLocators.FAVORITES_GOODS, timeout=1)

    def goods_must_be_in_favorites(self):
        assert self.is_element_present(*FavoritesPageLocators.FAVORITES_GOODS)

    def remove_goods_from_favorites(self):
        button = self.browser.find_element(*FavoritesPageLocators.BUTTON_DELETE_GOODS)
        button.click()

