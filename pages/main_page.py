from selenium.webdriver.common.by import By

from config.logger import setup_logger
from pages.base_form import BaseForm
from elements.button import Button
logger = setup_logger('MainPage')


class MainPage(BaseForm):
    __home_banner = (By.XPATH, '//*[@class="home-banner"]')
    __alerts_button = Button((By.XPATH, '//*[@class="card mt-4 top-card" and *//text()="Alerts, Frame & Windows"]'), "Alerts, Frame & Windows button")
    __elements_button = Button((By.XPATH, '//*[@class="card mt-4 top-card" and *//text()="Elements"]'), "Elements button")

    def __init__(self):
        logger.info('Initiating Main page')
        super().__init__(self.__home_banner, "Alerts Page")

    def go_to_alerts_window(self):
        logger.info('Going to Alerts, Frame & Windows')
        self.__alerts_button.click()

    def go_to_elements(self):
        logger.info('Going to Elements')
        self.__elements_button.click()
