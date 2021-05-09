from .locators import BasePageLocators
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def get_text_element(self, how, what):
        # получение текста из атрибута локатора
        return self.browser.find_element(how, what).text

    def should_be_login_link(self):
        # проверка, что на странице есть ссылка на страницу авторизации
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
        # переход на страницу авторизации
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_authorized_user(self):
        # проверка, что пользователь авторизован
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def go_to_basket_page(self):
        # переход на страницу корзины
        basket_link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        basket_link.click()

    def is_element_present(self, how, what):
        # проверка, что элемент присутствует на странице
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False

        return True

    def is_not_element_present(self, how, what, timeout=4):
        # проверка, что элемент не появляется на странице в течение заданного времени
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        # проверка, что элемент исчезает со страницы в течение заданного времени
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
