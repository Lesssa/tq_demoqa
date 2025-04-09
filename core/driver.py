from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from config.config_manager import ConfigManager
from config.logger import Logger
from core.singleton import Singleton
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class Driver(metaclass=Singleton):
    def __init__(self):
        Logger.info('Driver is initiating')
        super().__init__()
        self._driver = None
        self.base_url = ConfigManager.get("base_url")

    def __setup_driver(self):
        Logger.info('Setting up the driver')
        if self._driver is None:
            self._driver = self.__create_driver()
            self.__maximize_window()
        else:
            Logger.error("The driver is already set up")
            raise RuntimeError("The driver is already set up")

    def __maximize_window(self):
        Logger.info('Checking if window needs to be maximized and maximizing it if so')
        is_maximized = ConfigManager.get("browser_options.maximize")
        if is_maximized:
            self.driver.maximize_window()

    @staticmethod
    def __create_driver():
        Logger.info('Creating the driver')
        browser_name = ConfigManager.get("browser")
        options = Driver.__get_browser_options()
        if browser_name == "chrome":
            Logger.info('Chrome was chosen')
            return webdriver.Chrome(options)
        elif browser_name == "firefox":
            Logger.info('Firefox was chosen')
            return webdriver.Firefox(options)
        else:
            Logger.error('Chosen browser is not supported', exc_info=True)
            raise ValueError(f"Unsupported browser: {browser_name}")

    @staticmethod
    def __get_browser_options():
        Logger.info('Getting browser options from config')
        browser_name = ConfigManager.get("browser")
        if browser_name == "chrome":
            browser_options = ConfigManager.get("browser_options.chrome")
            options = ChromeOptions()
        elif browser_name == "firefox":
            browser_options = ConfigManager.get("browser_options.firefox")
            options = FirefoxOptions()
        else:
            Logger.error('Chosen browser is not supported', exc_info=True)
            raise ValueError(f"Unsupported browser: {browser_name}")
        for option in browser_options:
            options.add_argument(option)
        return options

# todo do smth to capabilities
    # @staticmethod
    # def __get_browser_capabilities():
    #     logger.info('Getting browser capabilities from config')
    #     browser_name = ConfigManager.get("browser")
    #     browser_options = ConfigManager.get("browser_options")
    #     if browser_name == "chrome":
    #         options = ChromeOptions()
    #     elif browser_name == "firefox":
    #         options = FirefoxOptions()
    #     else:
    #         logger.error('Chosen browser is not supported', exc_info=True)
    #         raise ValueError(f"Unsupported browser: {browser_name}")
    #     for option in browser_options:
    #         options.add_argument(option)
    #     return options

    @property
    def driver(self):
        Logger.info('Getting an instance of the driver')
        if self._driver is None:
            self.__setup_driver()
        return self._driver

    def quit(self):
        Logger.info('Quitting the browser and deleting the driver')
        if self._driver:
            self._driver.quit()
            self._driver = None
            Driver.remove_instance()

