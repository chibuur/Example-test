from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    
    def should_be_add_basket(self):
        #    self.add_to_basket();
        self.should_be_name_add_basket();
        self.should_be_price_basket();
    
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
    
#   def should_be_text_basket(self):
    #   assert self.is_element_present(*ProductPageLocators.MESS_ADD_BASKET), "Product don't added"
    
    def should_be_name_add_basket(self):
        name_messenge = self.browser.find_element(*ProductPageLocators.NAME_ADD_BASKET)
        product_name_add = name_messenge.text
        product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        assert product_name == product_name_add, "Wrong product added"
    
    def should_be_price_basket(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        assert price_product == price_basket, "Wrong price added"




