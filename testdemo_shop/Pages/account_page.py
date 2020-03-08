from .base_page import BasePage


class AccountPage(BasePage):
    ACCOUNT_TITLE = 'Your account'
    URL = 'https://autodemo.testoneo.com/en/my-account'
    LOGOUT_TEXT = 'Sign out'
