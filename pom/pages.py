from pom.base_page import BasePage
from pom.locators import (
    HomePageLocators,
    RegisterPageLocators,
    LoginPageLocators
)
from pom.components import HelpComponent


class HomePage(BasePage):
    """
    Class contains methods that represent the home page functionality
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HomePageLocators

    def click_home_button(self):
        """
        Click the 'HOME' button
        """
        self.wait_element_to_be_clickable(self.locator.HOME_BUTTON).click()
        return self

    def click_register_button(self):
        """
        Click the 'REGISTRATION' button
        """
        self.wait_element_to_be_clickable(self.locator.REGISTER_BUTTON).click()
        return RegisterPage(self.driver)

    def click_login_button(self):
        """
        Click the 'LOG IN' button
        """
        self.wait_element_to_be_clickable(self.locator.LOGIN_BUTTON).click()
        return LoginPage(self.driver)

    def click_reserve_button(self):
        """
        Click the 'Create Reservation' button
        """
        self.wait_element_to_be_clickable(self.locator.BOOK_BUTTON).click()
        return LoginPage(self.driver)

    def click_help_button(self):
        """
        Click the 'help ?'
        """
        self.wait_element_to_be_clickable(self.locator.HELP_BUTTON).click()
        return HelpComponent(self.driver)


class RegisterPage(BasePage):
    """
    Class contains methods that represent the registration page functionality
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = RegisterPageLocators

    def enter_username(self, username):
        """
        Enter your username in the 'Username' field
        """
        self.wait_element_to_be_clickable(self.locator.USERNAME_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.USERNAME_FIELD).clear()
        self.wait_element_to_be_clickable(self.locator.USERNAME_FIELD).send_keys(username)
        return self

    def enter_first_name(self, first_name):
        """
        Enter your first name in the 'Name' field
        """
        self.wait_element_to_be_clickable(self.locator.FIRST_NAME_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.FIRST_NAME_FIELD).clear()
        self.wait_element_to_be_clickable(self.locator.FIRST_NAME_FIELD).send_keys(first_name)
        return self

    def enter_last_name(self, last_name):
        """
        Enter your last name in the 'Surname' field
        """
        self.wait_element_to_be_clickable(self.locator.LAST_NAME_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.LAST_NAME_FIELD).clear()
        self.wait_element_to_be_clickable(self.locator.LAST_NAME_FIELD).send_keys(last_name)
        return self

    def enter_email(self, email):
        """
        Enter your email in the 'Email' field
        """
        self.wait_element_to_be_clickable(self.locator.EMAIL_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.EMAIL_FIELD).clear()
        self.wait_element_to_be_clickable(self.locator.EMAIL_FIELD).send_keys(email)
        return self

    def enter_password(self, password):
        """
        Enter your password in the 'Password' field
        """
        self.wait_element_to_be_clickable(self.locator.PASSWORD_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.PASSWORD_FIELD).clear()
        self.wait_element_to_be_clickable(self.locator.PASSWORD_FIELD).send_keys(password)
        return self

    def confirm_password(self, password):
        """
        Confirm your password in the 'Confirm password' field
        """
        self.wait_element_to_be_clickable(self.locator.CONFIRM_PASSWORD_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.CONFIRM_PASSWORD_FIELD).clear()
        self.wait_element_to_be_clickable(self.locator.CONFIRM_PASSWORD_FIELD).send_keys(password)
        return self

    def enter_phone(self, phone):
        """
        Enter your phone number in the 'Phone' field
        """
        self.wait_element_to_be_clickable(self.locator.PHONE_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.PHONE_FIELD).clear()
        self.wait_element_to_be_clickable(self.locator.PHONE_FIELD).send_keys(phone)
        return self

    def click_register_button(self):
        """
        Click the 'Register' button
        """
        self.wait_element_to_be_clickable(self.locator.REGISTER_BUTTON).click()
        return self


class LoginPage(BasePage):
    """
    Class contains methods that represent the login page functionality
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = LoginPageLocators

    def get_title(self):
        """
        Gets main title
        """
        return self.wait_element_to_appear(self.locator.LOGIN_TITLE).text

    def enter_username(self, username):
        """
        Enter your username in the 'Username' field
        """
        self.wait_element_to_be_clickable(self.locator.USERNAME_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.USERNAME_FIELD).clear()
        self.wait_element_to_be_clickable(self.locator.USERNAME_FIELD).send_keys(username)
        return self

    def enter_password(self, password):
        """
        Enter your password in the 'Password' field
        """
        self.wait_element_to_be_clickable(self.locator.PASSWORD_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.PASSWORD_FIELD).clear()
        self.wait_element_to_be_clickable(self.locator.PASSWORD_FIELD).send_keys(password)
        return self

    def click_submit_button(self):
        """
        Click the 'Submit' button
        """
        self.wait_element_to_be_clickable(self.locator.SUBMIT_BUTTON).click()
        return self
