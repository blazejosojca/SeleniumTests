import unittest

from Configuration import Config


class MainTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = Config().browser()

    def assert_element_text(self, xpath, expected_text):
        """
        Compare expected text with observed value from web element
        :param xpath: xpath to element with text to be observed
        :param expected_text: text what we expecting to be found
        :return: None
        """
        element = self.driver.find_element_by_xpath(xpath)
        return self.assertEqual(element.text, expected_text,
                                f'Expected message differ from {expected_text}')

    def assert_title(self, url, expected_text):
        self.driver.get(url)
        actual_title = self.driver.title
        self.assertEqual(expected_text, actual_title, f'Expected {expected_text} differ from actual driver,')

    @classmethod
    def tearDownClass(self):
        self.driver.close()
