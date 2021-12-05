import pytest
from selenium import webdriver

from pages.base_page import BasePage
from pages.favorites_page import FavoritesPage
from pages.main_page import MainPage


@pytest.mark.add_product
class TestInteractionsWithProductFromMainPage():
    @pytest.fixture(scope="function", autouse=True)
    def clean(self, browser):
        link = 'https://prom.ua/Velosipednye-shiny'
        page = BasePage(browser, link)
        page.open()
        page.login()
        page.should_be_authorized_user()
        page.go_to_favorites_page()

        f_page = FavoritesPage(browser, browser.current_url)
        f_page.goods_must_be_in_favorites()
        f_page.remove_goods_from_favorites()
        f_page.musnt_be_counter_favorites_goods()

    def test_user_can_add_goods_to_favorites_from_main_page(self, browser):
        link = 'https://prom.ua/Velosipednye-shiny'
        page = MainPage(browser, link)
        page.open()
        page.should_be_authorized_user()
        page.heart_is_not_filled_with_color()
        page.musnt_be_counter_favorites_goods()
        page.add_goods_to_favorites()
        page.must_be_counter_favorites_goods()

    def test_user_can_see_goods_in_favorites(self, browser):
        link = 'https://prom.ua/Velosipednye-shiny'
        page = MainPage(browser, link)
        page.open()
        page.heart_is_not_filled_with_color()
        page.add_goods_to_favorites()
        page.heart_is_filled_with_color()
        page.must_be_counter_favorites_goods()
        page.go_to_favorites_page()

        f_page = FavoritesPage(browser, browser.current_url)
        f_page.goods_must_be_in_favorites()
        f_page.must_be_counter_favorites_goods()

    def test_user_cant_see_goods_in_favorites(self, browser):
        link = 'https://prom.ua/Velosipednye-shiny'
        page = FavoritesPage(browser, link)
        page.favorites_must_be_empty()
        page.musnt_be_counter_favorites_goods()


@pytest.mark.check_correct_url
def test_user_be_in_the_correct_page(browser):
    link = 'https://prom.ua/Velosipednye-shiny'
    page = MainPage(browser, link)
    page.open()
    page.should_be_correct_name_category()


