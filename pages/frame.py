from config.logger import Logger
from core.driver import Driver
from pages.base_form import BaseForm
logger = Logger.get_logger()


class Frame(BaseForm):
    @staticmethod
    def switch_to_frame(locator):
        logger.info('Switching to a frame')
        Driver().driver.switch_to.frame(Driver().driver.find_element(*locator))

    @staticmethod
    def switch_to_default_content():
        logger.info('Switching to default container')
        Driver().driver.switch_to.default_content()
