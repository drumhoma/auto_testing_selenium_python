from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_from_product_page(self):
        self.should_be_add_to_basket_button()
        self.add_to_basket()
        self.should_be_name_in_basket()
        self.should_be_price_in_basket()

    def should_be_add_to_basket_button(self):
        # проверка, что кнопка добавить в корзину есть на странице
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET), "'Add to basket' button does not found"

    def add_to_basket(self):
        # добавление товара в корзину
        add_basket = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        add_basket.click()

    def should_be_name_in_basket(self):
        # проверка, что наименование товара в корзине соответствует наименованию на странице товара
        name = self.get_text_element(*ProductPageLocators.NAME)
        basket_name = self.get_text_element(*ProductPageLocators.BASKET_NAME)
        assert name == basket_name, "The item name in the basket is different"

    def should_be_price_in_basket(self):
        # проверка, что цена товара в корзине соответствует цене на странице товара
        price = self.get_text_element(*ProductPageLocators.PRICE)
        basket_price = self.get_text_element(*ProductPageLocators.BASKET_PRICE)
        assert price == basket_price, "The item price in the basket is different"

    def should_not_be_success_message(self):
        # проверка, что cообщение о добавлении товара в корзину не появилось
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but shouldn't"

    def should_be_disappear(self):
        # проверка, что cообщение о добавлении товара в корзину исчезло
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "The message should have disappeared, but didn't"
