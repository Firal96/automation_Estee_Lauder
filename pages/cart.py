from selenium.webdriver.common.by import By

from pages.base import Base

 
class CartPage(Base):
    URL = 'https://www.saucedemo.com/cart.html'
 
    # Locators
 
    ITEMS_NAME = (By.CSS_SELECTOR, '.inventory_item_name')
    CHECKOUT_BUTTON = (By.ID, 'checkout')

    # Initializer
 
    def __init__(self, browser):
        self.browser = browser
   
    # Interaction Methods
 
    def get_item_name(self):
        items_name = self.browser.find_element(*self.ITEMS_NAME).text
        return items_name

    def click_checkout_button(self):
        checkout_button = self.browser.find_element(*self.CHECKOUT_BUTTON)
        checkout_button.click()