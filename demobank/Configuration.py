import json
import os
from selenium.webdriver import Chrome, Firefox, Opera, Safari
from selenium.webdriver.opera.options import Options as opera_options
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as ff_options

from testdemo_shop.Helpers.functional_helper import load_json


CONFIG_FILE = 'config.json'
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
CONF_FILE_PATH = os.path.join(THIS_FOLDER, CONFIG_FILE)
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']
DEFAULT_HEADLESS_OPTION = ''

# rename the example.config.json to config.json


class Config(object):

    def config_browser(self):
        """
        Valid values for browser key
        :return: name of browser from data dict
        """
        data = load_json(CONF_FILE_PATH)
        if 'browser' not in data:
            raise Exception('The config file does not contain "browser"')
        elif data['browser'] not in SUPPORTED_BROWSERS:
            raise Exception(f'"{data["browser"]}" is not supported browser')
        return data['browser']

    def config_wait_time(self):
        """
        Verify and valid values from wait_time key
        :return:
        """
        data = load_json(CONF_FILE_PATH)
        return data['wait_time'] if 'wait_time' in data else DEFAULT_WAIT_TIME

    def headless_browser(self):
        data = load_json(CONF_FILE_PATH)
        return data['headless_option'] if 'headless_option' in data else DEFAULT_HEADLESS_OPTION

    def browser(self):
        config_browser = self.config_browser()
        config_wait_time = self.config_wait_time()
        config_headless = self.headless_browser()

        if config_browser == 'chrome':
            if config_headless == '--headless':
                driver_options = chrome_options()
                driver_options.headless = True
                driver = Chrome(options=driver_options)
            else:
                driver = Chrome()
        elif config_browser == 'firefox':
            if config_headless == '--headless':
                driver_options = ff_options()
                driver_options.headless = True
                driver = Firefox(options=driver_options)
            else:
                driver = Firefox()
        elif config_browser == 'opera':
            if config_headless == '--headless':
                driver_options = opera_options()
                driver_options.headless = True
                driver = Opera(options=driver_options)
            else:
                driver = Opera()
        else:
            raise Exception(f'"{config_browser}" is not a supported browser')

        driver.implicitly_wait(config_wait_time)

        return driver
