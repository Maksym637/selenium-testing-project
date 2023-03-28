from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.alert = Alert(driver)
        self.wait = WebDriverWait(driver, 20)
    
    def wait_element_to_appear(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def wait_element_to_be_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def wait_alert_to_appear(self):
        return self.wait.until(EC.alert_is_present())
    
    def click_alert_ok(self):
        return self.alert.accept()