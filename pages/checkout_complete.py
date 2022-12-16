from selenium.webdriver.common.by import By

from pages.base import Base

 
class CheckoutCompletePage(Base):
    URL = 'https://www.saucedemo.com/checkout-complete.html'
 
    # Locators
 
    TITLE_LABEL = (By.CSS_SELECTOR, ".title")

    # Initializer
 
    def __init__(self, browser):
        self.browser = browser
   
    # Interaction Methods
 
    def get_title_label(self):
        title_label = self.browser.find_element(*self.TITLE_LABEL)
        return title_label.text