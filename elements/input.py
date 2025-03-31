from config.logger import setup_logger
from elements.base_element import BaseElement
logger = setup_logger('Input')


class Input(BaseElement):
    def __init__(self, locator, name):
        logger.info('Initiating an input')
        super().__init__(locator, name)

    def send_keys(self, text):
        logger.info('Finding input and sending keys to it')
        self.find().send_keys(text)
