from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):
    """
    Main methods reused by other pages.
    """
    base_url = 'http://autodemo.testoneo.com/en/'

    def __init__(self, ef_driver):
        self.driver = ef_driver

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
