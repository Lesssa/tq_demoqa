from selenium.webdriver.common.by import By

from config.logger import setup_logger
from elements.button import Button
from pages.base_form import BaseForm
logger = setup_logger('BrowserPage')


class BrowserPage(BaseForm):
    __browser_window_block = (By.XPATH, '//*[@id="browserWindows"]')
    __new_tab_button = Button((By.XPATH, '//button[@id="tabButton"]'), 'New tab button')

    def __init__(self):
        logger.info('Initiating the browser window page')
        super().__init__(self.__browser_window_block, 'Browser Page')

    def get_new_tab_button(self):
        logger.info('Getting the button for opening a new tab')
        return self.__new_tab_button
