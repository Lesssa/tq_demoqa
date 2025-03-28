from selenium.webdriver.common.by import By

from pages.base_form import BaseForm
from elements.button import Button


class MainPage(BaseForm):
    __home_banner = (By.XPATH, '//*[@class="home-banner"]')
    __alerts_button = Button((By.XPATH, '//*[@class="card mt-4 top-card" and *//text()="Alerts, Frame & Windows"]'), "Alerts, Frame & Windows button")

    def __init__(self):
        super().__init__(self.__home_banner, "Alerts Page")

    def go_to_alerts(self):
        self.__alerts_button.click()
