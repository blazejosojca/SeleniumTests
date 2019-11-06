import unittest

from testdemo_shop.pages import LoginPage


def user_login(driver):
    """
    Use valid credentials email and password from class pages.LoginPage to login to account
    Password and login are declared in LoginPage
    :param driver: webdriver instance
    :return: None
    """
    login_page = LoginPage(driver)
    driver.get(login_page.login_url)
    login_page.login_with_valid_credentials()
