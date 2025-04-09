from selenium.webdriver.common.by import By
from config.logger import Logger
from elements.button import Button
from pages.base_form import BaseForm


class Header(BaseForm):
    __home_page = Button((By.XPATH, '//a[@href="https://demoqa.com"]'), 'Go to home page')

    def __init__(self):
        super().__init__(self.__home_page, 'Home Page Banner')

    def go_to_home(self):
        Logger.info('Going to home page')
        self.__home_page.click()
