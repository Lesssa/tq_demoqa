from selenium.webdriver.common.by import By

from config.logger import Logger
from elements.button import Button
from elements.label import Label
from pages.base_form import BaseForm


class LinkPage(BaseForm):
    __links_block = Label((By.XPATH, '//*[@id="linkWrapper"]'), "Links block")
    __home_link = Button((By.XPATH, '//a[@id="simpleLink"]'), 'Home link')

    def __init__(self):
        super().__init__(self.__links_block, 'Links Page')

    def get_home_link(self):
        Logger.info('Getting button for going to home')
        return self.__home_link
