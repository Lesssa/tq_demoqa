from abc import ABC
from selenium.webdriver.common.by import By

from config.logger import setup_logger
from elements.base_element import BaseElement
from elements.button import Button
logger = setup_logger('BaseForm')


class BaseForm(ABC):
    __home_page = Button((By.XPATH, '//a[@href="https://demoqa.com"]'), 'Go to home page')

    def __init__(self, locator, name):
        logger.info('Initiating a page')
        self.locator = locator
        self.name = name

    def is_displayed(self):
        logger.info(f'Checking if page is displayed')
        return BaseElement(self.locator, self.name).is_displayed()

    def go_to_home(self):
        logger.info('Going to home page')
        self.__home_page.click()
