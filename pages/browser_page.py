from selenium.webdriver.common.by import By

from config.logger import Logger
from elements.button import Button
from elements.label import Label
from pages.base_form import BaseForm


class BrowserPage(BaseForm):
    __browser_window_block = Label((By.XPATH, '//*[@id="browserWindows"]'), "Browser window block")
    __new_tab_button = Button((By.XPATH, '//button[@id="tabButton"]'), 'New tab button')

    def __init__(self):
        super().__init__(self.__browser_window_block, 'Browser Page')

    def click_new_tab_button(self):
        Logger.info('Clicking the button for opening a new tab')
        self.__new_tab_button.click()
