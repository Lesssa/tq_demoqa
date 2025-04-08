from selenium.webdriver.common.by import By

from config.logger import Logger
from elements.button import Button
from pages.base_form import BaseForm
logger = Logger.get_logger()


class BrowserPage(BaseForm):
    __browser_window_block = (By.XPATH, '//*[@id="browserWindows"]')
    __new_tab_button = Button((By.XPATH, '//button[@id="tabButton"]'), 'New tab button')

    def __init__(self):
        super().__init__(self.__browser_window_block, 'Browser Page')

    def click_new_tab_button(self):
        logger.info('clicking the button for opening a new tab')
        self.__new_tab_button.click()
