from abc import ABC

from config.logger import Logger


class BaseForm(ABC):
    def __init__(self, locator, name):
        self.__locator = locator
        self.__name = name

    def is_displayed(self):
        Logger.info('Checking if page is displayed')
        return self.__locator.is_displayed()

