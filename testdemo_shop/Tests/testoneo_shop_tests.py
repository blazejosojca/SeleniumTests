import unittest

from BaseTest import MainTest
from testdemo_shop.Helpers.functional_helper import user_login
from testdemo_shop.locators import (LoginPageLocators,
                                    AccountPageLocators,
                                    ArticlesPageLocators)
from testdemo_shop.Pages.login_page import LoginPage
from testdemo_shop.Pages.account_page import AccountPage


class SimpleTests(MainTest):

    def test_01_check_defined_header_is_on_login_site(self):
        expected_text = LoginPage.HEADER_TEXT
        self.driver.get(LoginPage.login_url)
        self.assert_element_text(LoginPageLocators.XPATH_HEADER_MESSAGE, expected_text)

    def test_02_check_login_to_registered_account_wrong_both_credentials(self):
        print(self.driver.current_url)
        login_page = LoginPage(self.driver)
        self.driver.get(login_page.login_url)
        login_page.login_with_invalid_credentials()
        print(self.driver.current_url)
        self.assert_element_text(LoginPageLocators.XPATH_AUTH_FAILED, LoginPage.FAILED_MESSAGE)

    def test_03_check_article_name(self):
        article_page = ArticlePage(self.driver)
        self.driver.get(article_page.URL)
        expected_name = 'HUMMINGBIRD PRINTED T-SHIRT'
        self.assert_element_text(ArticlesPageLocators.XPATH_ARTICLE_NAME, expected_name)

    def test_04_check_article_price(self):
        article_page = ArticlePage(self.driver)
        self.driver.get(article_page.URL)
        expected_price = 'PLN23.52'
        self.assert_element_text(ArticlesPageLocators.XPATH_ARTICLE_PRICE, expected_price)

    def test_05_check_login_to_registered_account(self):
        expected_header = AccountPage.ACCOUNT_TITLE
        user_login(self.driver)
        self.assert_element_text(AccountPageLocators.XPATH_ACCOUNT_HEADER, expected_header)


if __name__ == '__main__':
    unittest.main()
