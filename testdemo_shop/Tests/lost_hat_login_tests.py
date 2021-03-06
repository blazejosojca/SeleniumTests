import unittest

from testdemo_shop.BaseTest import BaseTestClass
from testdemo_shop.Helpers.functional_helper import user_login
from testdemo_shop.locators import AccountPageLocators, LoginPageLocators
from testdemo_shop.Pages.login_page import LoginPage
from testdemo_shop.Pages.register_page import RegisterPage
from testdemo_shop.Helpers.wrappers import screenshot_decorator



class LoginTests(BaseTestClass):

    @screenshot_decorator
    def test_01_check_defined_header_is_on_login_site(self):
        expected_text = LoginPage.HEADER_TEXT
        self.ef_driver.get(LoginPage.login_url)
        self.assert_element_text(LoginPageLocators.XPATH_HEADER_MESSAGE,
                                 expected_text)

    @screenshot_decorator
    def test_02_check_login_to_registered_account_wrong_both_credentials(self):
        page = LoginPage(self.ef_driver)
        self.ef_driver.get(page.login_url)
        page.login_with_invalid_credentials()
        self.assert_element_text(LoginPageLocators.XPATH_AUTH_FAILED,
                                 LoginPage.FAILED_MESSAGE)

    @screenshot_decorator
    def test_03_check_login_to_registered_account(self):
        user_login(self.ef_driver)
        self.assert_element_text(AccountPageLocators.XPATH_USER_NAME, RegisterPage.TEST_USER_NAME)


if __name__ == '__main__':
    unittest.main()
