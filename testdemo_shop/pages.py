from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from .locators import LoginPageLocators


class BasePage(object):
    """
    Main methods reused by other pages.
    """
    base_url = 'http://autodemo.testoneo.com/en/'

    def __init__(self, driver):
        self.driver = driver

    def find_and_fill_by_xpath(self, xpath, value):
        element = self.driver.find_element_by_xpath(xpath)
        element.clear()
        element.send_keys(value)

    def find_and_click_by_xpath(self, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        element.click()

    def scroll_find_and_wait_for_element(self, xpath, x_location, y_location):
        self.driver.execute_script("window.scrollTo('{0}', '{1}')".format(x_location, y_location))
        wait = WebDriverWait(self.driver, 2)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, xpath)))
        return element

    def get_page_title(self, url):
        self.driver.get(url)
        title = self.driver.title
        print(f"Actual title {title}")
        return title


# class HomePage(BasePage):
#     # main_url = BasePage.base_url
#     # _home_title = 'Lost Hat'

# class ClothesPage(BasePage):
#     clothes_url = BasePage.base_url + '3-clothes'
#     _clothes_title = 'Clothes'
#
# class AccessoriesPage(BasePage):
#     accessories_url = BasePage.base_url + '6-accessories'
#     _accessories_title = 'Accessories'

# class ArtsPage(BasePage):
#     art_url = BasePage.base_url + '9-art'
#     _art_title = 'Art'

class RegisterPage(BasePage):
    register_url = BasePage.base_url + '/login?create_account'
    TEST_SEX = 'Mr'
    TEST_FIRST_NAME = "John"
    TEST_SECOND_NAME = "Smith"
    TEST_EMAIL = "john.smith@mail.de"
    TEST_PASSWORD = "Password"
    TEST_USER_NAME = "John Smith"


# class LoginPage(BasePage):
#     _login_title = 'Login'
#     HEADER_TEXT = 'Log in to your account'
#     _url = 'https://autodemo.testoneo.com/en/login'
#     CORRECT_EMAIL = RegisterPage.TEST_EMAIL
#     CORRECT_PASSWORD = RegisterPage.TEST_PASSWORD
#     INCORRECT_EMAIL = 'wrong_admin@mail.com'
#     INCORRECT_PASSWORD = 'test_wrong_password'
#     FAILED_MESSAGE = 'Authentication failed.'
#
#     def user_login(self, email, password):
#         email_xpath = LoginPageLocators.XPATH_LOGIN_EMAIL_FIELD
#         password_xpath = LoginPageLocators.XPATH_LOGIN_PASSWORD_FIELD
#         sign_in_xpath = LoginPageLocators.XPATH_LOGIN_SIGNIN_BTN
#         self.find_and_fill_by_xpath(email_xpath, email)
#         self.find_and_fill_by_xpath(password_xpath, password)
#         self.find_and_click_by_xpath(sign_in_xpath)
#
#     def login_with_valid_credentials(self):
#         email = self.CORRECT_EMAIL
#         password = self.CORRECT_PASSWORD
#         self.user_login(email, password)
#
#     def login_with_invalid_credentials(self):
#         email = self.INCORRECT_EMAIL
#         password = self.INCORRECT_PASSWORD
#         self.user_login(email, password)


# class AccountPage(BasePage):
#     ACCOUNT_TITLE = 'Your account'
#     URL = 'https://autodemo.testoneo.com/en/my-account'
#     LOGOUT_TEXT = 'Sign out'


# class ArticlePage(BasePage):
#     URL = 'https://autodemo.testoneo.com/en/men/1-1-hummingbird-printed-t-shirt.html'
