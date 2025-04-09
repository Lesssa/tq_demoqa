from selenium.webdriver.common.by import By

from config.logger import Logger
from pages.base_form import BaseForm
from elements.button import Button


class MainPage(BaseForm):
    __home_banner = Button((By.XPATH, '//*[contains(@class, "home-banner")]'), "Home banner")
    __alerts_button = Button((By.XPATH, '//*[contains(@class, "card mt-4 top-card") and *//text()="Alerts, Frame & Windows"]'), "Alerts, Frame & Windows button")
    __elements_button = Button((By.XPATH, '//*[contains(@class, "card mt-4 top-card") and *//text()="Elements"]'), "Elements button")

    def __init__(self):
        super().__init__(self.__home_banner, "Alerts Page")

    def go_to_alerts_window(self):
        Logger.info('Going to Alerts, Frame & Windows')
        self.__alerts_button.click()

    def go_to_elements(self):
        Logger.info('Going to Elements')
        self.__elements_button.click()
