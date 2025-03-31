from selenium.webdriver.common.by import By

from config.logger import setup_logger
from elements.base_element import BaseElement
from pages.frame import Frame
logger = setup_logger('FramePage')


class FramePage(Frame):
    __upper_frame = (By.XPATH, '//*[@id="frame1"]')
    __lower_frame = (By.XPATH, '//*[@id="frame2"]')
    __frame_text = BaseElement((By.XPATH, '//*[@id="sampleHeading"]'), 'Frame text')

    def __init__(self):
        logger.info('Initiating a page with frames')
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
