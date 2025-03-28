from core.browser_factory import BrowserFactory
from core.singleton import Singleton


class Browser(metaclass=Singleton):
    def __init__(self):
        self.driver = BrowserFactory.create_driver()

    def get_driver(self):
        return self.driver

    def quit(self):
        if self.driver:
            self.driver.quit()
