import datetime
from selenium.webdriver.support.events import AbstractEventListener


class ScreenshotListener(AbstractEventListener):
    def on_exception(self, exception, driver):
        make_screenshot(driver, 'driver')


def make_screenshot(driver, producer):
    screenshot_path = f"TestResults/"
    screenshot_name = f"{producer}_screenshot_{datetime.datetime.now()}"
    driver.get_screenshot_as_file(f"{screenshot_path}/{screenshot_name}.png")
    print(f"Screenshot saved at {screenshot_path} as {screenshot_name}")

