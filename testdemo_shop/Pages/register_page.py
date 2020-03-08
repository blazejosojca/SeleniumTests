from .base_page import BasePage

class RegisterPage(BasePage):
    register_url = BasePage.base_url + '/login?create_account'
    TEST_SEX = 'Mr'
    TEST_FIRST_NAME = "John"
    TEST_SECOND_NAME = "Smith"
    TEST_EMAIL = "john.smith@mail.de"
    TEST_PASSWORD = "Password"
    TEST_USER_NAME = "John Smith"