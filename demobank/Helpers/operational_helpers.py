import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def wait_for_elements(driver, xpath_locator, max_wait_sec=5, number_of_expected_elems=1, error='Elements not found'):
    """Checking 1 second if list of elements under xpath > 0
          :param driver: webdriver instance
          :param xpath_locator: xpath of web element
          :param max_wait_sec: maximum_time_to_wait (default: 5)
          :param number_of_expected_elems: number of elements found (default: 1)
          :param error: error raised when elements not found
          :return: None
       """
    for second in range(max_wait_sec):
        elements = driver.find_elements_by_xpath(xpath_locator)

        print(f'Total waiting {second}s')

        if len(elements) >= number_of_expected_elems:
            return elements

        if second == (max_wait_sec - 1):
            print('End of wait')
            assert len(elements) > number_of_expected_elems, \
                f'Expected {number_of_expected_elems} elems but found {len(elements)}\
                 for xpath {xpath_locator} in time of {max_wait_sec}s'

        time.sleep(1)


def visibility_of_element_wait(driver, element_xpath, timeout=10):
    """
    Checking if specified by xpath element is visible on the page
    :param driver: webdriver instance
    :param element_xpath: xpath of web element
    :param timeout: time after looking for element will be stopped (default is 10 sec)
    :return: first element in list of found element
    """
    timeout_message =  f"Element for xpath: '{element_xpath}\n " \
                       f"and url : {driver.current_url} not found in {timeout} seconds"
    element_locator = (By.XPATH, element_xpath)
    element_wait = WebDriverWait(driver, timeout)
    element_located = EC.visibility_of_element_located(element_locator)

    return element_wait.until(element_located, timeout_message)
