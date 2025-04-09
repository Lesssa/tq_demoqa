from selenium.webdriver.common.by import By

from config.logger import Logger
from elements.label import Label
from pages.base_form import BaseForm
from pages.child_frame import ChildFrame
from pages.frame import Frame
from pages.parent_frame import ParentFrame


class NestedFramePage(BaseForm):
    __nested_frames_title = Label((By.XPATH, '//*[contains(@class, "text-center") and contains(text(), "Nested Frames")]'), "Nested frames title")
    __parent_frame = Label((By.XPATH, '//iframe[@id="frame1"]'), 'Parent frame')
    __child_frame = Label((By.XPATH, '//iframe[contains(@srcdoc, "Child Iframe")]'), 'Child frame')

    def __init__(self):
        super().__init__(self.__nested_frames_title, "Nested Frames Page")
        self.parent_frame = ParentFrame()
        self.child_frame = ChildFrame()

    def get_parent_text(self):
        Logger.info('Getting parent frame text')
        with Frame(self.__parent_frame):
            parent_text = self.parent_frame.get_text()
        return parent_text

    def get_child_text(self):
        Logger.info('Getting child frame text')
        with Frame(self.__parent_frame):
            with Frame(self.__child_frame):
                child_text = self.child_frame.get_text()

        return child_text
