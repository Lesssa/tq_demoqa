from config.logger import Logger
from core.driver import Driver


class Frame:
    def __init__(self, frame_locator):
        self.__frame_locator = frame_locator

    def __enter__(self):
        Logger.info("Switching to frame")
        Driver().driver.switch_to.frame(self.__frame_locator.find())

    def __exit__(self, exc_type, exc_val, exc_tb):
        Logger.info("Exiting frame, switching back to the parent context")
        Driver().driver.switch_to.default_content()

