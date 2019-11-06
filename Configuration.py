import json
import os
from selenium.webdriver import Chrome, Firefox, Opera


CONFIG_FILE = 'config.json'
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
CONF_FILE_PATH = os.path.join(THIS_FOLDER, CONFIG_FILE)
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']


class Config(object):

    def config(self):
        """
        Load data from json.config and return to further reuse.
        :return: dictionary with keys and values from json config file.
        """
        with open(CONF_FILE_PATH) as config_file:
            data = json.load(config_file)
        return data

    def config_browser(self):
        """
        Valid values for browser key
        :return: name of browser from data dict
        """
        data = self.config()
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
        data = self.config()
        return data['wait_time'] if 'wait_time' in data else DEFAULT_WAIT_TIME

    def browser(self):
        config_browser = self.config_browser()
        config_wait_time = self.config_wait_time()
        if config_browser == 'chrome':
            driver = Chrome()
        elif config_browser == 'firefox':
            driver = Firefox()
        elif config_browser == 'opera':
            driver = Opera()
        else:
            raise Exception(f'"{config_browser}" is not a supported browser')

        driver.implicitly_wait(config_wait_time)

        return driver