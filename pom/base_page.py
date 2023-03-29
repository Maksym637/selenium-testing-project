from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from utils.constants import TimeoutVariables


class BasePage:
    """
    Superclass with all explicit waits
    """

    def __init__(self, driver):
        self.driver = driver
        self.alert = Alert(driver)
        self.wait = WebDriverWait(driver, TimeoutVariables.EXPLICIT_WAIT.value)

    def wait_element_to_appear(self, locator):
        """
        Waits element to appeare on the page
        """
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_element_to_be_clickable(self, locator):
        """
        Waits element to be clickable on the page
        """
        return self.wait.until(EC.element_to_be_clickable(locator))

    def get_alert_message(self):
        """
        Gets an error message from the alert window
        """
        return self.wait.until(EC.alert_is_present()).text

    def click_alert_ok(self):
        """
        Click the 'OK' button in the alert window
        """
        return self.alert.accept()
