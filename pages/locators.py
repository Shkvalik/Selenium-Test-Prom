from selenium.webdriver.common.by import By


class BasePageLocators():
    BUTTON_FAVORITES = (By.CSS_SELECTOR, "button[aria-label='Избранное']")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "button[class='_2KaCs']")
    BUTTON_LOGIN_BY_EMAIL = (By.CSS_SELECTOR, "div[data-qaid='email_btn']")
    INPUT_LOGIN = (By.CSS_SELECTOR, "input[id='email_field']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[id='enterPassword']")
    BUTTON_CONFIRM_INPUT_LOGIN = (By.CSS_SELECTOR, "button[id='emailConfirmButton']")
    BUTTON_CONFIRM_INPUT_PASSWORD = (By.CSS_SELECTOR, "button[id='enterPasswordConfirmButton']")
    COUNTER_FAVORITES_GOODS = (By.CSS_SELECTOR, "div[data-qaid='counter']")
    BUTTON_CABINET = (By.CSS_SELECTOR, "button[data-qaid='menu_btn']")


class MainPageLocators():
    PART_NAME_CATEGORY_URL = 'Velosipednye-shiny'
    BUTTON_ADD_TO_FAVORITES = (By.CSS_SELECTOR, "div[class='GWc_y _3V5Rw _1u0_W'] div[class='yJNOx']")
    HEART = (By.XPATH, "//div[@class='GWc_y _3V5Rw _1u0_W']/div[@class='yJNOx']//*[local-name() = 'path']")


class FavoritesPageLocators():
    PART_FAVORITES_URL = 'favorites'
    FAVORITES_GOODS = (By.CSS_SELECTOR, "div[data-qaid='favorite_row']")
    BUTTON_DELETE_GOODS = (By.CSS_SELECTOR, "span[data-qaid='delete_icon']")


class GoodsPageLocators():
    PART_GOODS_NAME_URL = 'pokrishka-schwalbe-marathon'
    BUTTON_ADD_TO_FAVORITES = (By.CSS_SELECTOR, "div[class='GWc_y _1yIYf _3V5Rw'] span[data-qaid='add_favorite']")
    HEART = (By.XPATH, "//div[@class='GWc_y _1yIYf _3V5Rw']/div[@class='yJNOx']//*[local-name() = 'path']")