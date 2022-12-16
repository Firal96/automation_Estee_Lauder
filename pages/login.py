from selenium.webdriver.common.by import By
from pages.base import Base
 
class LoginPage(Base):
    URL = 'https://www.saucedemo.com/'
 
    # Locators
 
    USER_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
 
    # Initializer
 
    def __init__(self, browser):
        self.browser = browser
   
    # Interaction Methods
 
    def fill_login(self, user, password):
        user_input = self.browser.find_element(*self.USER_INPUT)
        user_input.send_keys(user)
        password_input = self.browser.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)
        enter_button = self.browser.find_element(*self.LOGIN_BUTTON)
        enter_button.click()