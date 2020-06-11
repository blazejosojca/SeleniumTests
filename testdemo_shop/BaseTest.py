import unittest
import datetime

from testdemo_shop.Configuration import Config

from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from testdemo_shop.Helpers.screenshot_listener import ScreenshotListener


class BaseTestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Config().browser()
        print("Run started at:" + str(datetime.datetime.utcnow()))
        cls.ef_driver = EventFiringWebDriver(cls.driver, ScreenshotListener())

    def assert_element_text(self, xpath, expected_text):
        """
        Compare expected text with observed value from web element
        :param xpath: xpath to element with text to be observed
        :param expected_text: text what we expecting to be found
        :return: None
        """
        element = self.ef_driver.find_element_by_xpath(xpath)
        return self.assertEqual(element.text, expected_text,
                                f'Expected message differ from {expected_text}')

    def assert_element_contains_innerText(self, selector, expected_text):
        """
        Compare expected text with observed value from web elements
        :param selector: css_selector to list with elements to be observed
        :param expected_text: text what we expecting to be found in element from the list
        :return: assertions for every element
        """
        elements = self.ef_driver.find_elements_by_css_selector(selector)
        for element in elements:
            return self.assertIn(element.get_attribute('innerText'), expected_text,
                                 f'Expected message differ from {expected_text}')

    def assert_title(self, url, expected_text):
        self.ef_driver.get(url)
        actual_title = self.ef_driver.title
        self.assertEqual(expected_text, actual_title, f'Expected {expected_text} differ from actual driver,')

    def go_driver_give_that_page(self, driver, url, page_object):
        tested_page = page_object(driver)
        driver.get(url)
        return tested_page


    @classmethod
    def tearDownClass(cls):
        cls.ef_driver.quit()
        if (cls.ef_driver != None):
            print("Test environment destroyed.")
            print("Run completed at: " + str(datetime.datetime.utcnow()))



    """
        @classmethod
    def setUpClass(self):
        self.driver = Config().browser()
        print("Run started at:" + str(datetime.datetime.utcnow()))
        self.ef_driver = EventFiringWebDriver(self.driver, ScreenshotListener())
        self.ef_driver.maximize_window()

        
    @classmethod
    def tearDownClass(self):
        self.ef_driver.quit()
        if self.ef_driver is not None:  
            print("Test environment destroyed.")
            print("Run completed at: " + str(datetime.datetime.utcnow()))
    """
