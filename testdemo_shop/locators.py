class RegisterPageLocators(object):
    XPATH_HEADER_CREATE_ACCOUNT =''
    XPATH_TITLE_MR = ''
    XPATH_FIRST_NAME = ''
    XPATH_LAST_NAME = ''
    XPATH_EMAIL = ''
    XPATH_PASSWORD = ''
    XPATH_BIRTH_DATE = ''
    XPATH_CHECKBOX_OFFERS = ''
    XPATH_CHECKBOX_NEWSLETTER = ''
    XPATH_SAVE_BUTTON = ''


class LoginPageLocators(object):
    XPATH_HEADER_MESSAGE = '//section/header/h1'
    XPATH_LOGIN_EMAIL_FIELD = '//input[@class = "form-control"]'
    XPATH_LOGIN_PASSWORD_FIELD = '//input[@name = "password"]'
    XPATH_LOGIN_SIGNIN_BTN = '//button[@id = "submit-login"]'
    XPATH_AUTH_FAILED = '//li[@class="alert alert-danger"]'


class ArticlesPageLocators(object):
    XPATH_ARTICLE_NAME = '//h1[@itemprop="name"]'
    XPATH_ARTICLE_PRICE = '//span[@itemprop="price"]'


class AccountPageLocators(object):
    XPATH_ACCOUNT_HEADER = '//header[@class="page-header"]/h1'
    CSS_SIGN_OUT = '.logout'
    XPATH_USER_NAME = '//a[@class="account"]/*[@class="hidden-sm-down"]'


class HomePageLocators(object):
    CSS_SLIDER = '#carousel.carousel'
    CSS_SLIDER_ELEMENTS = '.carousel-item'
    XPATH_SLIDES_TITLES = '//*[@id="carousel"]/ul/li//*[contains(@class, "text-uppercase")]'
    CSS_SLIDES_TITLES = 'h2.text-uppercase'
    CSS_ARTICLE_MINIATURE = 'article.product-miniature.js-product-miniature'
