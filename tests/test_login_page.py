from parameterized import parameterized
from pom.pages import HomePage
from tests.base_test import BaseTest

ALERT_MSG = "[INVALID PASSWORD OR USERNAME]"


class TestLoginPage(BaseTest):
    """
    Class contains tests that are on the login page
    """

    @parameterized.expand([
        ("undefined", "undefined", ALERT_MSG),
        ("username2", " ", ALERT_MSG),
        (" ", "password3", ALERT_MSG),
        (" ", " ", ALERT_MSG)
    ])
    def test_login_incorrect(self, username, password, expected_alert_msg):
        """
        This test verifies if an alert window with the appropriate 
        error message appears after entering incorrect data
        """
        home_page = HomePage(self.driver)

        actual_alert_msg = (
            home_page
            .click_login_button()
            .enter_username(username)
            .enter_password(password)
            .click_submit_button()
            .get_alert_message()
        )

        home_page.click_alert_ok()

        self.assertEqual(actual_alert_msg, expected_alert_msg)
