from parameterized import parameterized
from pom.pages import HomePage
from tests.base_test import BaseTest

ALERT_MSG = [
    "[PASSWORD ARE NOT SIMILAR]",
    "[THIS PASSWORD IS TOO SHORT]",
    "[THIS PASSWORD IS VERY SIMPLE]"
]


class TestRegisterPage(BaseTest):
    """
    Class contains tests that are on the registration page
    """

    @parameterized.expand([
        ("user1", "user1", "user1", "user1@gmail.com",
         "some text 1", "some text 2", 1212121212, ALERT_MSG[0]),
        ("user2", "user2", "user2", "user2@gmail.com",
         "abc", "abc", 1212121212, ALERT_MSG[1]),
        ("user3", "user3", "user3", "user3@gmail.com",
         11111111, 11111111, 1212121212, ALERT_MSG[2])
    ])
    def test_register_incorrect(self, username, first_name, last_name, email,
                                password, confirmation, phone, expected_alert_msg):
        """
        This test verifies if an alert window with the appropriate error message appears
        after entering incorrect data in the password and confirm password fields
        """
        home_page = HomePage(self.driver)

        actual_alert_msg = (
            home_page
            .click_register_button()
            .enter_username(username)
            .enter_first_name(first_name)
            .enter_last_name(last_name)
            .enter_email(email)
            .enter_password(password)
            .confirm_password(confirmation)
            .enter_phone(phone)
            .click_register_button()
            .get_alert_message()
        )

        home_page.click_alert_ok()

        self.assertEqual(actual_alert_msg, expected_alert_msg)
