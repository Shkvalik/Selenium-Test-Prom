from selenium.webdriver.common.by import By


class BasePageLocators():
    BUTTON_FAVORITE = (By.CSS_SELECTOR, "button[aria-label='Избранное']")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "button[class='_2KaCs']")
    BUTTON_LOGIN_BY_EMAIL = (By.CSS_SELECTOR, "div[data-qaid='email_btn']")
    INPUT_LOGIN = (By.CSS_SELECTOR, "input[id='email_field']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[id='enterPassword']")
    BUTTON_CONFIRM_INPUT_LOGIN = (By.CSS_SELECTOR, "button[id='emailConfirmButton']")
    BUTTON_CONFIRM_INPUT_PASSWORD = (By.CSS_SELECTOR, "button[id='enterPasswordConfirmButton']")
    COUNTER_FAVORITE_GOODS = (By.CSS_SELECTOR, "div[class='_1Ol4v']")
    BUTTON_CABINET = (By.CSS_SELECTOR, "button[data-qaid='menu_btn']")

class MainPageLocators():
    NAME_CATEGORY = 'Velosipednye-shiny'
    BUTTON_ADD_TO_FAVORITE = (By.CSS_SELECTOR, "div[class='GWc_y _3V5Rw _1u0_W'] div[class='yJNOx']")
    HEART = (By.XPATH, "//*[local-name() = 'path']")