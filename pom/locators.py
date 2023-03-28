from selenium.webdriver.common.by import By


class HomePageLocators:
    REGISTER_BUTTON = (By.XPATH, "//a[@href='/register']")
    LOGIN_BUTTON = (By.XPATH, "//a[@href='/login']")
    BOOK_BUTTON = (By.XPATH, "//a[@href='/book']")
    HELP_BUTTON = (By.XPATH, "//i[contains(text(), 'help ?')]")


class HelpComponentLocators:
    DESCRIPTION_TITLE = (By.XPATH, "//div[@id='popup']//div[@class='popup__title']")
    SOME_TEXT = (By.XPATH, "//div[@id='popup']//p[1]")


class RegisterPageLocators:
    USERNAME_FIELD = (By.XPATH, "//input[@data-testid='username']")
    FIRST_NAME_FIELD = (By.XPATH, "//input[@data-testid='first_name']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@data-testid='last_name']")
    EMAIL_FIELD = (By.XPATH, "//input[@data-testid='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@data-testid='password']")
    CONFIRM_PASSWORD_FIELD = (By.XPATH, "//input[@data-testid='confirm-password']")
    PHONE_FIELD = (By.XPATH, "//input[@data-testid='phone']")
    REGISTER_BUTTON = (By.XPATH, "//input[@class='register']")


class LoginPageLocators:
    LOGIN_TITLE = (By.XPATH, "//div[@class='title_login']//i")
    USERNAME_FIELD = (By.XPATH, "//input[@data-testid='username']")
    PASSWORD_FIELD = (By.XPATH, "//input[@data-testid='password']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@class='submit']")
