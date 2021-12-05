import pytest

from pages.base_page import BasePage
from pages.favorites_page import FavoritesPage
from pages.goods_page import GoodsPage


@pytest.mark.add_product
class TestInteractionsWithProductFromProductPage():
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

    def test_user_can_add_goods_to_favorites_from_product_page(self, browser):
        link = 'https://prom.ua/p712545800-pokrishka-schwalbe-marathon.html'
        page = GoodsPage(browser, link)
        page.open()
        page.should_be_authorized_user()
        page.heart_is_not_filled_with_color()
        page.musnt_be_counter_favorites_goods()
        page.add_goods_to_favorites()
        page.must_be_counter_favorites_goods()


@pytest.mark.check_correct_url
def test_user_be_in_the_correct_page(browser):
    link = 'https://prom.ua/p712545800-pokrishka-schwalbe-marathon.html'
    page = GoodsPage(browser, link)
    page.open()
    page.must_be_correct_name_category()