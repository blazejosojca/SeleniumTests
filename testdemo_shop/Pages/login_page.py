from testdemo_shop.Pages.base_page import BasePage
from testdemo_shop.locators import LoginPageLocators
from testdemo_shop.Locators.login_page_locs import LoginPageLocators
from testdemo_shop.Pages import register_page


class LoginPage(BasePage):
    _login_title = 'Login'
    HEADER_TEXT = 'Log in to your account'
    login_url = 'https://autodemo.testoneo.com/en/login'
    CORRECT_EMAIL = register_page.RegisterPage.TEST_EMAIL
    CORRECT_PASSWORD = register_page.RegisterPage.TEST_PASSWORD
    INCORRECT_EMAIL = 'wrong_admin@mail.com'
    INCORRECT_PASSWORD = 'test_wrong_password'
    FAILED_MESSAGE = 'Authentication failed.'

    def user_login(self, email, password):
        email_xpath = LoginPageLocators.XPATH_LOGIN_EMAIL_FIELD
        password_xpath = LoginPageLocators.XPATH_LOGIN_PASSWORD_FIELD
        sign_in_xpath = LoginPageLocators.XPATH_LOGIN_SIGNIN_BTN
        self.find_and_fill_by_xpath(email_xpath, email)
        self.find_and_fill_by_xpath(password_xpath, password)
        self.find_and_click_by_xpath(sign_in_xpath)

    def login_with_valid_credentials(self):
        email = self.CORRECT_EMAIL
        password = self.CORRECT_PASSWORD
        self.user_login(email, password)

    def login_with_invalid_credentials(self):
        email = self.INCORRECT_EMAIL
        password = self.INCORRECT_PASSWORD
        self.user_login(email, password)