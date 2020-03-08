from demobank.Pages.base_page import BasePage

class LoginPage(BasePage):
    _title = 'Demobank - Bankowość Internetowa - Logowanie'
    _url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'


    # def user_login(self, email, password):
    #     email_xpath = LoginPageLocators.XPATH_LOGIN_EMAIL_FIELD
    #     password_xpath = LoginPageLocators.XPATH_LOGIN_PASSWORD_FIELD
    #     sign_in_xpath = LoginPageLocators.XPATH_LOGIN_SIGNIN_BTN
    #     self.find_and_fill_by_xpath(email_xpath, email)
    #     self.find_and_fill_by_xpath(password_xpath, password)
    #     self.find_and_click_by_xpath(sign_in_xpath)
    #
    # def login_with_valid_credentials(self):
    #     email = self.CORRECT_EMAIL
    #     password = self.CORRECT_PASSWORD
    #     self.user_login(email, password)
    #
    # def login_with_invalid_credentials(self):
    #     email = self.INCORRECT_EMAIL
    #     password = self.INCORRECT_PASSWORD
    #     self.user_login(email, password)