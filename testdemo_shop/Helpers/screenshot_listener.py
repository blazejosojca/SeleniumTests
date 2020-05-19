import datetime
from selenium.webdriver.support.events import AbstractEventListener


class ScreenshotListener(AbstractEventListener):

    def on_exception(self, exception, driver):

        screenshot_path = f"../TestResults"
        screenshot_name = f"screenshot_{datetime.datetime.now()}"
        driver.get_screenshot_as_file(f"{screenshot_path}/{screenshot_name}.png")
        print(f"Screenshot saved as {screenshot_name}")


