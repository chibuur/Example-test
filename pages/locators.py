from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main>p.price_color")
    MESS_ADD_BASKET = (By.CSS_SELECTOR, ".alert-success:nth-child(1)>.alertinner")
    NAME_ADD_BASKET = (By.CSS_SELECTOR, ".alert-success:nth-child(1)>.alertinner>strong")
    PRICE_BASKET = (By.CSS_SELECTOR, ".alert-info>.alertinner>p>strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main>h1")
