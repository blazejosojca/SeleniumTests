import unittest

from testdemo_shop.BaseTest import BaseTestClass
from testdemo_shop.Helpers.functional_helper import user_login
from testdemo_shop.locators import (LoginPageLocators,
                                    AccountPageLocators,
                                    ArticlesPageLocators,
                                    )
from testdemo_shop.Pages.login_page import LoginPage
from testdemo_shop.Pages.account_page import AccountPage
from testdemo_shop.Pages.article_sub_page import ArticleSubPage

from testdemo_shop.Helpers.wrappers import screenshot_decorator


class SimpleTests(BaseTestClass):

    @screenshot_decorator
    def test_01_check_defined_header_is_on_login_site(self):
        expected_text = LoginPage.HEADER_TEXT
        self.ef_driver.get(LoginPage.login_url)
        self.assert_element_text(LoginPageLocators.XPATH_HEADER_MESSAGE, expected_text)

    @screenshot_decorator
    def test_02_check_login_to_registered_account_wrong_both_credentials(self):
        print(self.ef_driver.current_url)
        login_page = LoginPage(self.ef_driver)
        self.ef_driver.get(login_page.login_url)
        login_page.login_with_invalid_credentials()
        print(self.ef_driver.current_url)
        self.assert_element_text(LoginPageLocators.XPATH_AUTH_FAILED, LoginPage.FAILED_MESSAGE)

    @screenshot_decorator
    def test_03_check_article_name(self):
        article_page = ArticleSubPage(self.ef_driver)
        self.ef_driver.get(article_page.URL)
        expected_name = 'HUMMINGBIRD PRINTED T-SHIRT'
        self.assert_element_text(ArticlesPageLocators.XPATH_ARTICLE_NAME, expected_name)

    @screenshot_decorator
    def test_04_check_article_price(self):
        article_page = ArticleSubPage(self.ef_driver)
        self.ef_driver.get(article_page.URL)
        expected_price = 'PLN23.52'
        self.assert_element_text(ArticlesPageLocators.XPATH_ARTICLE_PRICE, expected_price)

    @screenshot_decorator
    def test_05_check_login_to_registered_account(self):
        expected_header = AccountPage.ACCOUNT_TITLE
        user_login(self.ef_driver)
        self.assert_element_text(AccountPageLocators.XPATH_ACCOUNT_HEADER, expected_header)


if __name__ == '__main__':
    unittest.main()
