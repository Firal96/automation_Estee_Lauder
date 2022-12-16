from selenium.webdriver.common.by import By

from pages.base import Base

 
class CheckoutPage(Base):
    URL = 'https://www.saucedemo.com/checkout-step-one.html'
 
    # Locators
 
    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    ZIP_INPUT = (By.ID, 'postal-code')
    ITEM_NAME_LABEL = (By.CSS_SELECTOR, '.inventory_item_name')
    CONTINUE_BUTTON = (By.ID, 'continue')
    FINISH_BUTTON = (By.ID, 'finish')

    # Initializer
 
    def __init__(self, browser):
        self.browser = browser
   
    # Interaction Methods
 
    def fill_name(self, name):
        first_name_input = self.browser.find_element(*self.FIRST_NAME_INPUT)
        first_name_input.send_keys(name)

    def fill_last_name(self, lastname):
        last_name_input = self.browser.find_element(*self.LAST_NAME_INPUT)
        last_name_input.send_keys(lastname)

    def fill_zip(self, zip):
        zip_input = self.browser.find_element(*self.ZIP_INPUT)
        zip_input.send_keys(zip)

    def click_continue_button(self):
        continue_button = self.browser.find_element(*self.CONTINUE_BUTTON)
        continue_button.click()

    def get_item_name(self):
        items_name = self.browser.find_element(*self.ITEM_NAME_LABEL).text
        return items_name

    def click_finish_button(self):
        finish_button = self.browser.find_element(*self.FINISH_BUTTON)
        finish_button.click()