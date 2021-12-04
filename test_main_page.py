import pytest
from selenium import webdriver
from pages.main_page import MainPage


def test_user_be_in_the_correct_page(browser):
    link = 'https://prom.ua/Velosipednye-shiny'
    page = MainPage(browser, link)
    page.open()
    page.should_be_correct_name_category()


def test_user_can_add_goods_to_favorite(browser):
    link = 'https://prom.ua/Velosipednye-shiny'
    page = MainPage(browser, link)
    page.open()
    page.login()
    page.should_be_authorized_user()
    page.add_good_to_favorites()
    page.heart_is_filled_with_color()
    page.should_be_counter_favorite_goods()