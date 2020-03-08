import unittest

from BaseTest import MainTest
from testdemo_shop.Helpers.functional_helper import user_login
from testdemo_shop.locators import AccountPageLocators, LoginPageLocators
from testdemo_shop.Pages import login_page, register_page


class LoginTests(MainTest):

    def test_01_check_defined_header_is_on_login_site(self):
        expected_text = login_page.LoginPage.HEADER_TEXT
        self.driver.get(login_page.LoginPage.login_url)
        self.assert_element_text(LoginPageLocators.XPATH_HEADER_MESSAGE,
                                 expected_text)

    def test_02_check_login_to_registered_account_wrong_both_credentials(self):
        print(self.driver.current_url)
        page = login_page.LoginPage(self.driver)
        self.driver.get(page.login_url)
        login_page.login_with_invalid_credentials()
        print(self.driver.current_url)
        self.assert_element_text(LoginPageLocators.XPATH_AUTH_FAILED,
                                 login_page.LoginPage.FAILED_MESSAGE)

    def test_03_check_login_to_registered_account(self):
        user_login(self.driver)
        self.assert_element_text(AccountPageLocators.XPATH_USER_NAME, register_page.RegisterPage.TEST_USER_NAME)



if __name__ == '__main__':
    unittest.main()
