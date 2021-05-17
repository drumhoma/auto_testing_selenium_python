from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.XPATH, "//i[@class='icon-user']")


class BasketPageLocators:
    BASKET_LINK = (By.XPATH, "//a[@class='btn btn-default']")
    EMPTY_BASKET = (By.XPATH, "//div[@id='content_inner']/p")


class MainPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTER_FORM = (By.XPATH, "//form[@id='register_form']")

    REG_EMAIL = (By.XPATH, "//input[@name='registration-email']")
    REG_PASS = (By.XPATH, "//input[@name='registration-password1']")
    REG_CONFIRM_PASS = (By.XPATH, "//input[@name='registration-password2']")
    REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")


class ProductPageLocators:
    ADD_BASKET = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")

    NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRICE = (By.XPATH, "//p[@class='price_color']")

    BASKET_NAME = (By.XPATH, "//div[1]/div[@class='alertinner ']/strong")
    BASKET_PRICE = (By.XPATH, "//div[@class='alertinner ']/p/strong")

    SUCCESS_MESSAGE = (By.XPATH, "//div[1][@class='alert alert-safe alert-noicon alert-success  fade in']")
