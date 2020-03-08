from BaseTest import MainTest

from demobank.Pages.login_page import LoginPage
from demobank.Pages.transfer_page import TransferPage
from demobank.Pages.desktop_page import DesktopPage
from demobank.Pages.account_page import AccountPage

class LoginTests(MainTest):

    def test_demo_login(self):
        self.driver.get(LoginPage._url)
        expected_login_page_title = 'Demobank - Bankowość Internetowa - Logowanie'
        self.assert_title(LoginPage._url,
                          expected_login_page_title)

    def test_demo_accounts(self):
        self.driver.get(AccountPage._url)
        expected_account_page_title = 'Demobank - Bankowość Internetowa - Konta'
        self.assert_title(AccountPage._url,
                          expected_account_page_title)

    def test_demo_pulpit(self):
        self.driver.get(DesktopPage._url)
        expected_desktop_page_title = 'Demobank - Bankowość Internetowa - Pulpit'
        self.assert_title(DesktopPage._url,
                          expected_desktop_page_title)

    def test_demo_transfer(self):
        self.driver.get(TransferPage._url)
        expected_desktop_page_title = 'Demobank - Bankowość Internetowa - Przelew'
        self.assert_title(TransferPage._url, expected_desktop_page_title)
