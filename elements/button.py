from config.logger import Logger
from elements.base_element import BaseElement
logger = Logger.get_logger('Button')


class Button(BaseElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)


