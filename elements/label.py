from config.logger import Logger
from elements.base_element import BaseElement
logger = Logger.get_logger('Input')


class Label(BaseElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)

