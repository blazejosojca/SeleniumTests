from selenium.common.exceptions import TimeoutException

from Helpers.screenshot_listener import make_screenshot

def screenshot_decorator(test_function):
    def wrapper(self):
        try:
            return test_function(self)
        except AssertionError as ex:
            make_screenshot(self.ef_driver, "assertion")
            raise ex
        except TimeoutException as ex:
            make_screenshot(self.ef_driver, "timeout")
            raise ex

    return wrapper
