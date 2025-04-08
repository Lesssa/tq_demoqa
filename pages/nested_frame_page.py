from selenium.webdriver.common.by import By

from config.logger import Logger
from elements.base_element import BaseElement
from elements.label import Label
from pages.frame import Frame
logger = Logger.get_logger()


# todo locators are not unique
# todo parent shouldn't be frame, it's a page
class NestedFramePage(Frame):
    __parent_frame = (By.XPATH, '//iframe[@id="frame1"]')
    __child_frame = (By.XPATH, "//iframe")
    __parent_text = Label((By.XPATH, "//body[iframe]"), 'Parent text')
    __child_text = Label((By.XPATH, "//p"), 'Child Text')

    def __init__(self):
        super().__init__(self.__parent_frame, "Nested Frames Page")

    def get_parent_text(self):
        logger.info('Getting parent frame text')
        self.switch_to_frame(self.__parent_frame)
        text = self.__parent_text.get_text()
        self.switch_to_default_content()
        return text

    def get_child_text(self):
        logger.info('Getting child frame text')
        self.switch_to_frame(self.__parent_frame)
        self.switch_to_frame(self.__child_frame)
        text = self.__child_text.get_text()
        self.switch_to_default_content()
        return text
