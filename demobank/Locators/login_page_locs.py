class LoginPageLocators(object):
    XPATH_HEADER = '//*[@id="login_form"]/h1'
    XPATH_LOGIN_INPUT_FIELD = '//*[@id="login_id"]'
    XPATH_LOGIN_PASSWORD_FIELD = '//*[@id="login_password"]'
    XPATH_LOGIN_SIGNIN_BTN = '//button[@id = "submit-login"]'
    XPATH_AUTH_FAILED = '//li[@class="alert alert-danger"]'
    XPATH_NEXT_BUTTON = '//*[@id="login_next"]'
    XPATH_POPUP = '//*[@class="shadowbox-content contact-popup"]/div/h2'
    XPATH_MESSAGE = '//*[@id="show_messages"]'
