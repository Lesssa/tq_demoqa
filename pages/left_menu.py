from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from config.config_manager import ConfigManager
from config.logger import setup_logger
from core.driver import Driver
from elements.button import Button
from pages.base_form import BaseForm
from selenium.webdriver.support import expected_conditions as EC
logger = setup_logger('LeftMenu')


class LeftMenu(BaseForm):
    __left_panel = (By.XPATH, '//*[@class="left-pannel"]')
    __alerts_button = Button((By.XPATH, '//*[@class="card mt-4 top-card" and *//text()="Alerts, Frame & Windows"]'),
                             "Alerts, Frame & Windows button")
    __go_to_alerts = Button((By.XPATH, '//*[@id="item-1" and *//text()="Alerts"]'), "Left panel alerts button")
    __go_to_nested_frames = Button((By.XPATH, '//*[@id="item-3" and *//text()="Nested Frames"]'),
                                   'Left panel nested frames button')
    __go_to_frames = Button((By.XPATH, '//*[@id="item-2" and *//text()="Frames"]'), 'Left panel frames button')
    __go_to_web_tables = Button((By.XPATH, '//*[@id="item-3" and *//text()="Web Tables"]'), 'Left panel web tables button')
    __go_to_browser_windows = Button((By.XPATH, '//*[@id="item-0" and *//text()="Browser Windows"]'), 'Left panel browser windows button')
    __go_to_links = Button((By.XPATH, '//*[@id="item-5" and *//text()="Links"]'), 'Left panel links button')
    __open_elements_list = Button((By.XPATH, '//*[@class="header-wrapper" and *//text()="Elements"]'), 'Elements list')
    __elements_are_shown = (By.XPATH, '//*[@class="element-list collapse show"]')

    def __init__(self):
        logger.info('Initiating left menu')
        super().__init__(self.__left_panel, 'Left Menu')

    def go_to_alerts_window(self):
        logger.info('Going to Alerts, Frame & Windows')
        self.__alerts_button.click()

    def go_to_alerts(self):
        logger.info('Going to alerts page')
        self.__go_to_alerts.click()

    def go_to_nested_frames(self):
        logger.info('Going to nested frames page')
        self.__go_to_nested_frames.click()

    def go_to_frames(self):
        logger.info('Going to frames page')
        self.__go_to_frames.click()

    def go_to_web_tables(self):
        logger.info('Going to web tables page')
        self.__go_to_web_tables.click()

    def go_to_browser_windows(self):
        logger.info('Going to browser windows page')
        self.__go_to_browser_windows.click()

    def go_to_links(self):
        logger.info('Going to links page')
        self.__go_to_links.click()

    def open_elements_list(self):
        logger.info('Expanding Elements list')
        self.__open_elements_list.click()

    def wait_shown_list(self):
        logger.info('Waiting for Elements items to be revealed')
        return WebDriverWait(Driver().get_driver, ConfigManager.get('waiting_time')).until(
            EC.presence_of_element_located(self.__elements_are_shown)
        )
