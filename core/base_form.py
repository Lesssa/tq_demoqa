from abc import ABC

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser import Browser


class BaseForm(ABC):
    def __init__(self, locator, name):
        self.locator = locator
        self.name = name

    def is_displayed(self):
        return WebDriverWait(Browser.get_driver(), 10).until(
            EC.presence_of_element_located(self.locator)
        )