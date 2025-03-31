from config.logger import setup_logger
from core.driver import Driver
from pages.base_form import BaseForm
logger = setup_logger('Frame')


class Frame(BaseForm):
    @staticmethod
    def switch_to_frame(locator):
        logger.info('Switching to a frame')
        Driver().get_driver.switch_to.frame(Driver().get_driver.find_element(*locator))

    @staticmethod
    def switch_to_default_content():
        logger.info('Switching to default container')
        Driver().get_driver.switch_to.default_content()
