from pom.pages import HomePage
from tests.base_test import BaseTest
from parameterized import parameterized

ALERT_MSG = "[INVALID PASSWORD OR USERNAME]"


class TestLoginPage(BaseTest):

    @parameterized.expand([
        ("undefined", "undefined", ALERT_MSG),
        ("username2", " ", ALERT_MSG),
        (" ", "password3", ALERT_MSG),
        (" ", " ", ALERT_MSG)
    ])
    def test_login_incorrect(self, username, password, expected_alert_msg):
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
