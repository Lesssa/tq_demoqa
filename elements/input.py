from config.logger import Logger
from elements.base_element import BaseElement
logger = Logger.get_logger('Input')


class Input(BaseElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)

    def send_keys(self, text):
        logger.info('Finding input and sending keys to it')
        self.find().send_keys(text)
