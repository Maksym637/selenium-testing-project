from pom.base_page import BasePage
from pom.locators import HelpComponentLocators


class HelpComponent(BasePage):
    """
    Class contains methods that represent the help component functionality
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HelpComponentLocators

    def get_text(self):
        """
        Gets text from the help window
        """
        return self.wait_element_to_appear(self.locator.SOME_TEXT).text
