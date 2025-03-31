from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config_manager import ConfigManager
from config.logger import setup_logger
from core.driver import Driver
logger = setup_logger('BaseElement')


class BaseElement:
    def __init__(self, locator, name):
        logger.info('Initiating an element')
        self.locator = locator
        self.name = name

    def find(self):
        logger.info('Trying to find an element on a page')
        return WebDriverWait(Driver().get_driver, ConfigManager.get('waiting_time')).until(
            EC.visibility_of_element_located(self.locator)
        )

    def move_to(self):
        logger.info('Scrolling the page to see an element')
        element = self.find()
        Driver().get_driver.execute_script("arguments[0].scrollIntoView(true);", element)
        action = ActionChains(Driver().get_driver)
        action.move_to_element(element).perform()

    def get_text(self):
        logger.info('Getting a text from an element')
        return self.find().text

    def is_displayed(self):
        logger.info(f'Checking if an element is displayed')
        try:
            element = self.find()
            return element.is_displayed()
        except:
            logger.warning(f'Element isn\'t displayed')
            return False
