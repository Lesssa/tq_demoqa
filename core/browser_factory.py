from selenium import webdriver

from config.config_manager import ConfigManager


class BrowserFactory:
    @staticmethod
    def create_driver():
        browser_name = ConfigManager.get("browser")
        if browser_name == "chrome":
            return webdriver.Chrome()
        elif browser_name == "firefox":
            return webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
