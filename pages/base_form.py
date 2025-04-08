from abc import ABC
from selenium.webdriver.common.by import By

from config.logger import Logger
from elements.base_element import BaseElement
from elements.button import Button
logger = Logger.get_logger()

# todo remove button
class BaseForm(ABC):
    __home_page = Button((By.XPATH, '//a[@href="https://demoqa.com"]'), 'Go to home page')

    def __init__(self, locator, name):
        self.__locator = locator
        self.__name = name

    def is_displayed(self):
        logger.info(f'Checking if page is displayed')
        return BaseElement(self.__locator, self.__name).is_displayed()


