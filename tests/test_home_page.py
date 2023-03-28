from tests.base_test import BaseTest
from pom.pages import HomePage


class TestHomePage(BaseTest):

    def test_help_window(self):
        home_page = HomePage(self.driver)

        actual_text = (
            home_page
            .click_home_button()
            .click_help_button()
            .get_text()
        )
        
        self.assertEqual(actual_text, "2.) You have ability to edit and delete your reservation.")
    
    def test_create_reservation(self):
        home_page = HomePage(self.driver)

        actual_title = (
            home_page
            .click_home_button()
            .click_reserve_button()
            .get_title()
        )

        self.assertEqual(actual_title, "Login Form")
