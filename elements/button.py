from config.logger import setup_logger
from elements.base_element import BaseElement
logger = setup_logger('Button')


class Button(BaseElement):
    def __init__(self, locator, name):
        logger.info('Initiating a button')
        super().__init__(locator, name)

    def click(self):
        logger.info('Scrolling to the button and clicking it')
        self.move_to()
        self.find().click()
