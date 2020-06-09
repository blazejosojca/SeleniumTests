import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def wait_for_elements(driver, xpath_locator, max_wait_sec=5, number_of_elems=1,
                      error='Elements not found'):
    """Checking 1 second if list of elements under xpath > 0
          :param driver: webdriver instance
          :param xpath_locator: xpath of web element
          :param max_wait_sec: maximum_time_to_wait (default: 5)
          :param number_of_elems: number of elements found (default: 1)
          :param error: error raised when elements not found
          :return: None
       """
    for second in range(max_wait_sec):
        elements = driver.find_elements_by_xpath(xpath_locator)
        print(f'Total waiting {second}s')

        if len(elements) >= number_of_elems:
            return elements

        if second == (max_wait_sec - 1):
            print('End of wait')
            assert (len(elements) > number_of_elems,\
                     f"Expected {number_of_elems} elems but found {len(elements)}\
                    for xpath {xpath_locator} in time of {max_wait_sec}s")
        time.sleep(1)


def visibility_of_element_wait(driver, loc_type, element_path, timeout=10):
    """
    Checking if specified by xpath element is visible on the page
    :param driver: webdriver instance
    :param loc_type: strings 'css' or 'xpath' are allowed
    :param element_path: xpath of web element
    :param timeout: time after looking for element will be stopped (default is 10 sec)
    :return: first element in list of found element
    """
    timeout_message =  f"Element path: '{element_path}\n " \
                       f"and url : {driver.current_url} not found in {timeout} seconds"
    try:
        if loc_type == 'css':
            element_locator = (By.CSS_SELECTOR, element_path)
        elif loc_type == 'xpath':
            element_locator = (By.XPATH, element_path)
    except ValueError as error:
        print(error)
    finally:
        element_located = EC.visibility_of_element_located(element_locator)
        element_wait = WebDriverWait(driver.wrapped_driver, timeout)  # using pure driver
    return element_wait.until(element_located, timeout_message)
