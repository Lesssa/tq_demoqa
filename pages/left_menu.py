from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from config.config_manager import ConfigManager
from config.logger import Logger
from core.driver import Driver
from elements.button import Button
from elements.label import Label
from pages.base_form import BaseForm


class LeftMenu(BaseForm):
    __left_panel = Label((By.XPATH, '//*[contains(@class, "left-pannel")]'), "Left panel")
    __alerts_button = Button((By.XPATH, '//*[contains(@class, "card mt-4 top-card") and *//text()="Alerts, Frame & Windows"]'),
                             "Alerts, Frame & Windows button")
    __go_to_alerts = Button((By.XPATH, '//*[text()="Alerts"]'), "Left panel alerts button")
    __go_to_nested_frames = Button((By.XPATH, '//*[text()="Nested Frames"]'),
                                   'Left panel nested frames button')
    __go_to_frames = Button((By.XPATH, '//*[text()="Frames"]'), 'Left panel frames button')
    __go_to_web_tables = Button((By.XPATH, '//*[text()="Web Tables"]'), 'Left panel web tables button')
    __go_to_browser_windows = Button((By.XPATH, '//*[text()="Browser Windows"]'), 'Left panel browser windows button')
    __go_to_links = Button((By.XPATH, '//*[text()="Links"]'), 'Left panel links button')
    __open_elements_list = Button((By.XPATH, '//*[contains(@class, "header-wrapper") and *//text()="Elements"]'), 'Elements list')
    __elements_are_shown = Label((By.XPATH, '//*[contains(@class, "element-list collapse show")]'), 'Elements are shown')

    def __init__(self):
        super().__init__(self.__left_panel, 'Left Menu')

    def go_to_alerts_window(self):
        Logger.info('Going to Alerts, Frame & Windows')
        self.__alerts_button.click()

    def go_to_alerts(self):
        Logger.info('Going to alerts page')
        self.__go_to_alerts.click()

    def go_to_nested_frames(self):
        Logger.info('Going to nested frames page')
        self.__go_to_nested_frames.click()

    def go_to_frames(self):
        Logger.info('Going to frames page')
        self.__go_to_frames.click()

    def go_to_web_tables(self):
        Logger.info('Going to web tables page')
        self.__go_to_web_tables.click()

    def go_to_browser_windows(self):
        Logger.info('Going to browser windows page')
        self.__go_to_browser_windows.click()

    def go_to_links(self):
        Logger.info('Going to links page')
        self.__go_to_links.click()

    def open_elements_list(self):
        Logger.info('Expanding Elements list')
        self.__open_elements_list.click()

    def wait_shown_list(self):
        Logger.info('Waiting for Elements items to be revealed')
        return self.__elements_are_shown.is_displayed()
