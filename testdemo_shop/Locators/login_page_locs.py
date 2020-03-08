class LoginPageLocators(object):
    XPATH_HEADER_MESSAGE = '//section/header/h1'
    XPATH_LOGIN_EMAIL_FIELD = '//input[@class = "form-control"]'
    XPATH_LOGIN_PASSWORD_FIELD = '//input[@name = "password"]'
    XPATH_LOGIN_SIGNIN_BTN = '//button[@id = "submit-login"]'
    XPATH_AUTH_FAILED = '//li[@class="alert alert-danger"]'