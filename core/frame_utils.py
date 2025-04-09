from config.logger import Logger
from core.driver import Driver


class FrameUtils:
    @staticmethod
    def switch_to_frame(frame_element):
        Logger.info('Switching to a frame')
        Driver().driver.switch_to.frame(frame_element.find())

    @staticmethod
    def switch_to_default_content():
        Logger.info('Switching to default container')
        Driver().driver.switch_to.default_content()
