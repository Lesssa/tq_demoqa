from selenium import webdriver
from config.config_manager import ConfigManager
from config.logger import setup_logger
from core.singleton import Singleton
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
logger = setup_logger('Driver')


class Driver(metaclass=Singleton):
    def __init__(self):
        logger.info('Driver is initiating')
        super().__init__()
        self._driver = None
        self.base_url = ConfigManager.get("base_url")
        self.__setup_driver()

    def __setup_driver(self):
        logger.info('Setting up the driver')
        if self._driver is None:
            self._driver = self.__create_driver()
            self.get_driver.get(self.base_url)

    @staticmethod
    def __create_driver():
        logger.info('Creating the driver')
        browser_name = ConfigManager.get("browser")
        options = Driver.__get_browser_options()
        if browser_name == "chrome":
            logger.info('Chrome was chosen')
            return webdriver.Chrome(options)
        elif browser_name == "firefox":
            logger.info('Firefox was chosen')
            return webdriver.Firefox(options)
        else:
            logger.error('Chosen browser is not supported', exc_info=True)
            raise ValueError(f"Unsupported browser: {browser_name}")

    @staticmethod
    def __get_browser_options():
        logger.info('Getting browser options from config')
        options = None
        browser_name = ConfigManager.get("browser")
        browser_options = ConfigManager.get("browser_options")
        if browser_name == "chrome":
            options = ChromeOptions()
        elif browser_name == "firefox":
            options = FirefoxOptions()
        for option in browser_options:
            options.add_argument(option)
        return options

    @property
    def get_driver(self):
        logger.info('Getting an instance of the driver')
        if self.__setup_driver() is None:
            self.__setup_driver()
        return self._driver

    def quit(self):
        logger.info('Quitting the browser and deleting the driver')
        if self._driver:
            self._driver.quit()
            self._driver = None
            Driver.remove_instance()

