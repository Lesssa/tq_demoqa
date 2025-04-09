from selenium.webdriver.common.by import By

from config.logger import Logger
from elements.label import Label
from pages.base_form import BaseForm


class ChildFrame(BaseForm):
    __inner_text = Label((By.XPATH, '//*[contains(text(), "Child Iframe")]'), "Child frame inner text")

    def __init__(self):
        super().__init__(self.__inner_text, "Child frame")

    def get_text(self):
        Logger.info("Getting text from child frame")
        return self.__inner_text.get_text()