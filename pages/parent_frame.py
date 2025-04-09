from selenium.webdriver.common.by import By

from config.logger import Logger
from elements.label import Label
from pages.base_form import BaseForm


class ParentFrame(BaseForm):
    __inner_text = Label((By.XPATH, '//*[contains(text(), "Parent frame")]'), "Parent frame inner text")

    def __init__(self):
        super().__init__(self.__inner_text, "Parent frame")

    def get_text(self):
        Logger.info("Getting text from parent frame")
        return self.__inner_text.get_text()
