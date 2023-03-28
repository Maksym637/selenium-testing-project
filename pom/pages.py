from pom.base_page import BasePage
from pom.locators import (
    HomePageLocators,
    RegisterPageLocators,
    LoginPageLocators
)


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HomePageLocators
    
    def click_regiter_button(self):
        self.wait_element_to_be_clickable(self.locator.REGISTER_BUTTON).click()
        return RegisterPage(self.driver)
    
    def click_login_button(self):
        self.wait_element_to_be_clickable(self.locator.LOGIN_BUTTON).click()
        return LoginPage(self.driver)


class RegisterPage(BasePage):
    pass


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = LoginPageLocators
    
    def enter_username(self, username):
        self.wait_element_to_be_clickable(self.locator.USERNAME_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.USERNAME_FIELD).clear()
        self.wait_element_to_be_clickable(self.locator.USERNAME_FIELD).send_keys(username)
        return self
    
    def enter_password(self, password):
        self.wait_element_to_be_clickable(self.locator.PASSWORD_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.PASSWORD_FIELD).clear()
        self.wait_element_to_be_clickable(self.locator.PASSWORD_FIELD).send_keys(password)
        return self
    
    def click_submit_button(self):
        self.wait_element_to_be_clickable(self.locator.SUBMIT_BUTTON).click()
        return self
    
    def get_alert_message(self):
        return self.wait_alert_to_appear().text
