from pom.pages import HomePage
from tests.base_test import BaseTest


class TestHomePage(BaseTest):
    """
    Class contains tests that are on the home page
    """

    def test_help_window(self):
        """
        This test verifies if a pop-up window is 
        opened after clicking the 'help ?' button
        """
        home_page = HomePage(self.driver)

        actual_text = (
            home_page
            .click_home_button()
            .click_help_button()
            .get_text()
        )

        self.assertEqual(actual_text, "2.) You have ability to edit and delete your reservation.")

    def test_create_reservation(self):
        """
        This test case verifies if a user is redirected to Login Page 
        after clicking the 'Create Reservation' button
        """
        home_page = HomePage(self.driver)

        actual_title = (
            home_page
            .click_home_button()
            .click_reserve_button()
            .get_title()
        )

        self.assertEqual(actual_title, "Login Form")
