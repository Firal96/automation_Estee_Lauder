from selenium.webdriver.common.by import By

from pages.base import Base

import random

 
class InventoryPage(Base):
    URL = 'https://www.saucedemo.com/inventory.html'
 
    # Locators
 
    ITEMS_LIST = (By.CSS_SELECTOR, '.inventory_item')
    CART_BUTTON = (By.CSS_SELECTOR, '.shopping_cart_link')

    # Initializer
 
    def __init__(self, browser):
        self.browser = browser
   
    # Interaction Methods
 
    def select_random_item(self):
        items_list = self.browser.find_elements(*self.ITEMS_LIST)
        item = items_list[random.randint(0,5)]
        item_name = item.find_element(By.CSS_SELECTOR, '.inventory_item_name').text
        item_button = item.find_element(By.CSS_SELECTOR, '.btn')
        item_button.click()
        return item_name

    def click_cart(self):
        cart_button = self.browser.find_element(*self.CART_BUTTON)
        cart_button.click()