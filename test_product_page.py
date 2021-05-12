import time

import pytest

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

link_common = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
link_promo = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


@pytest.mark.guest_add_basket_from_product
class TestAddBasketFromProductPage():
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link_promo)
        page.open()
        page.should_be_add_to_basket_button()
        page.add_to_basket()
        page.solve_quiz_and_get_code()  # опционально - прохождение алерта
        page.should_be_name_in_basket()
        page.should_be_price_in_basket()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link_common)
        page.open()
        page.add_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message_wo_add_to_basket(self, browser):
        page = ProductPage(browser, link_common)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link_common)
        page.open()
        page.add_to_basket()
        page.should_be_disappear()


@pytest.mark.guest_can_login_from_product_page
class TestLoginFromProductPage():
    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, link_common)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link_common)
        page.open()
        page.go_to_login_page()


@pytest.mark.guest_cant_see_product_in_basket
class TestEmptyBasketForGuest():
    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, link_common)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_product_in_basket()
        basket_page.should_be_empty_basket()
        basket_page.should_be_text_empty_basket()


@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.io"
        password = ("RanD0m_Pa55w0Rd!")
        registration = LoginPage(browser, link_common)
        registration.open()
        registration.go_to_login_page()
        registration.register_new_user(email, password)
        registration.should_be_authorized_user()

    def test_user_cant_see_success_message_wo_add_to_basket(self, browser):
        page = LoginPage(browser, link_common)
        page = ProductPage(browser, link_common)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.debug
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link_common)
        page.open()
        page.should_be_add_to_basket_button()
        page.add_to_basket()
        page.should_be_name_in_basket()
        page.should_be_price_in_basket()
