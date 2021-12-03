import pytest
from selenium import webdriver
from pages.main_page import MainPage


def test_user_be_in_the_correct_page(browser):
    link = 'https://prom.ua/Velosipednye-shiny'
    page = MainPage(browser, link)
    page.open()
    page.should_be_correct_name_category()
# full heart = //*[local-name() = 'path'][@d='M10 3.09C8.91 1.81 7.24 1 5.5 1 2.42 1 0 3.42 0 6.5c0 3.78 3.4 6.86 8.55 11.54L10 19.35l1.45-1.32C16.6 13.36 20 10.28 20 6.5 20 3.42 17.58 1 14.5 1c-1.74 0-3.41.81-4.5 2.09z']
# not full = //*[local-name() = 'path'][@d='M14.5 1c-1.74 0-3.41.81-4.5 2.09C8.91 1.81 7.24 1 5.5 1 2.42 1 0 3.42 0 6.5c0 3.78 3.4 6.86 8.55 11.54L10 19.35l1.45-1.32C16.6 13.36 20 10.28 20 6.5 20 3.42 17.58 1 14.5 1zm-4.4 15.55l-.1.1-.1-.1C5.14 12.24 2 9.39 2 6.5 2 4.5 3.5 3 5.5 3c1.54 0 3.04.99 3.57 2.36h1.87C11.46 3.99 12.96 3 14.5 3c2 0 3.5 1.5 3.5 3.5 0 2.89-3.14 5.74-7.9 10.05z']
