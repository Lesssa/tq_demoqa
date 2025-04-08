from selenium.webdriver.common.by import By

from config.logger import Logger
from elements.base_element import BaseElement
from elements.label import Label
from pages.base_form import BaseForm
from pages.frame import Frame
logger = Logger.get_logger()


# todo after changing to baseform there's some errors
class FramePage(BaseForm):
    __upper_frame = (By.XPATH, '//*[@id="frame1"]')
    __lower_frame = (By.XPATH, '//*[@id="frame2"]')
    __frame_text = Label((By.XPATH, '//*[@id="sampleHeading"]'), 'Frame text')

    def __init__(self):
        super().__init__(self.__upper_frame, "Frames Page")

    def get_upper_frame_text(self):
        logger.info('Getting text from upper frame')
        self.switch_to_frame(self.__upper_frame)
        text = self.__frame_text.get_text()
        self.switch_to_default_content()
        return text

    def get_lower_frame_text(self):
        logger.info('Getting text from lower frame')
        self.switch_to_frame(self.__lower_frame)
        text = self.__frame_text.get_text()
        self.switch_to_default_content()
        return text
