from selenium.webdriver.common.by import By

from config.logger import Logger
from elements.base_element import BaseElement
from elements.label import Label
from pages.base_form import BaseForm
from pages.frame import Frame
from pages.sample_page import SamplePage


class FramePage(BaseForm):
    __frames_title = Label((By.XPATH, '//*[contains(@class, "text-center") and contains(text(), "Frames")]'), "Frames title")
    __upper_frame = Label((By.XPATH, '//*[@id="frame1"]'), 'Upper frame')
    __lower_frame = Label((By.XPATH, '//*[@id="frame2"]'), 'Lower frame')

    def __init__(self):
        super().__init__(self.__frames_title, "Frames Page")
        self.sample_frame = SamplePage()

    def get_upper_frame_text(self):
        Logger.info('Getting text from upper frame')
        with Frame(self.__upper_frame):
            text = self.sample_frame.get_text()
        return text

    def get_lower_frame_text(self):
        Logger.info('Getting text from lower frame')
        with Frame(self.__lower_frame):
            text = self.sample_frame.get_text()
        return text
