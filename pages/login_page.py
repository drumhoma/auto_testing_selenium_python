from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        # проверка наличия элементов авторизации и регистрации
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка, что открыта страница регистрации/авторизации
        url = self.browser.current_url
        assert "login" in url, "'Login' is not contain in URL"

    def should_be_login_form(self):
        # проверка, что на странице есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not exists"

    def should_be_register_form(self):
        # проверка, что на странице есть форма регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not exists"

    def register_new_user(self, email, password):
        # регистрация нового пользователя
        email_enter = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        email_enter.send_keys(email)

        password_enter = self.browser.find_element(*LoginPageLocators.REG_PASS)
        password_enter.send_keys(password)

        confirm_password_enter = self.browser.find_element(*LoginPageLocators.REG_CONFIRM_PASS)
        confirm_password_enter.send_keys(password)

        registration = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        registration.click()
