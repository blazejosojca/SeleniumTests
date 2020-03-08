import unittest

from BaseTest import MainTest
from testdemo_shop.Helpers.functional_helper import user_login
from testdemo_shop.locators import (AccountPageLocators, ArticlesPageLocators,
                                    HomePageLocators, LoginPageLocators)
from testdemo_shop.pages import AccountPage, ArticlePage, HomePage, LoginPage


class PageTests(MainTest):

    def test_01_check_login_to_registered_account(self):
        expected_header = AccountPage.ACCOUNT_TITLE
        user_login(self.driver)
        self.assert_element_text(AccountPageLocators.XPATH_ACCOUNT_HEADER, expected_header)


if __name__ == '__main__':
    unittest.main()
