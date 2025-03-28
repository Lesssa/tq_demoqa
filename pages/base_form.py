from abc import ABC

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.browser import Browser
from elements.button import Button


class BaseForm(ABC):
    def __init__(self, locator, name):
        self.locator = locator
        self.name = name

    def is_displayed(self):
        return Button(self.locator).is_displayed()