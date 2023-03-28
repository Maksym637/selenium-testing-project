from pom.base_page import BasePage
from pom.locators import HelpComponentLocators


class HelpComponent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HelpComponentLocators
    
    def get_text(self):
        return self.wait_element_to_appear(self.locator.SOME_TEXT).text
