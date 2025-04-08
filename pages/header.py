from selenium.webdriver.common.by import By
from config.logger import Logger
from elements.button import Button

logger = Logger.get_logger()


class Header():
    __home_page = Button((By.XPATH, '//a[@href="https://demoqa.com"]'), 'Go to home page')

    def go_to_home(self):
        logger.info('Going to home page')
        self.__home_page.click()