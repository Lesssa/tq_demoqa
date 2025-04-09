from selenium.webdriver.common.by import By

from config.logger import Logger
from elements.label import Label
from pages.base_form import BaseForm


class SamplePage(BaseForm):
    __sample_text = Label((By.XPATH, '//*[@id = "sampleHeading"]'), "Sample page text")

    def __init__(self):
        super().__init__(self.__sample_text, "Sample Page")

    def get_text(self):
        Logger.info("Getting text from frame")
        return self.__sample_text.get_text()
