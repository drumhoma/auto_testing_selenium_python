from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        # проверка, что корзина пуста
        self.should_be_empty_basket()
        self.should_be_text_empty_basket()

    def should_be_empty_basket(self):
        # проверка, что в корзине нет товаров
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "Basket is not empty"

    def should_be_text_empty_basket(self):
        # проверка, что есть текст о том, что корзина пуста
        assert self.get_text_element(*BasketPageLocators.EMPTY_BASKET) != 0, "No text 'Your basket is empty'"
