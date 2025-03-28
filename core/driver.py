from selenium import webdriver
from config.config_manager import ConfigManager
from core.singleton import Singleton


class Driver(metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self._driver = None
        self.base_url = ConfigManager.get("base_url")
        self.__setup_driver()

    def __setup_driver(self):
        if self._driver is None:
            self._driver = self.__create_driver()
            self.get_driver.get(self.base_url)
            # if self.config.maximize_window:
            #     self._driver.maximize_window()

    @staticmethod
    def __create_driver():
        browser_name = ConfigManager.get("browser")
        if browser_name == "chrome":
            return webdriver.Chrome()
        elif browser_name == "firefox":
            return webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

    @property
    def get_driver(self):
        if self.__setup_driver() is None:
            self.__setup_driver()
        return self._driver

    def quit(self):
        if self._driver:
            self._driver.quit()
            self._driver = None
            Driver.remove_instance()

