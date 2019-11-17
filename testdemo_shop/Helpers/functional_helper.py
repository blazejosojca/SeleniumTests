import unittest
import json

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




def load_json(path):
    """
    Load data from json.load_json and return to further reuse.
    :return: dictionary with keys and values from json load_json file.
    """
    with open(path) as file:
        data = json.load(file)
    return data

