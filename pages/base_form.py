from abc import ABC

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.driver import Driver
from elements.base_element import BaseElement
from elements.button import Button


class BaseForm(ABC):
    def __init__(self, locator, name):
        self.locator = locator
        self.name = name

    def is_displayed(self):
        return BaseElement(self.locator, self.name).is_displayed()

