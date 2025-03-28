from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from core.driver import Driver
from elements.button import Button
from pages.base_form import BaseForm


class AlertsPage(BaseForm):
    # RENAME VARS
    __left_panel = (By.XPATH, '//*[@class="left-pannel"]')
    __showed_alerts_panel = (By.XPATH, '//*[@class="element-group" and .//text()[contains(., "Alerts, Frame & Windows")]]//*[@class="element-list collapse show"]')
    __go_to_alerts = Button((By.XPATH, '//*[@id="item-1" and *//text()="Alerts"]'), "Left panel alerts button")
    __alerts_title = (By.XPATH, '//*[@id="javascriptAlertsWrapper"]')
    __alert_button = Button((By.XPATH, '//button[@id="alertButton"]'), 'Alert button')

    def __init__(self):
        super().__init__(self.__showed_alerts_panel, 'Alerts Page')

    def go_to_alerts(self):
        self.__go_to_alerts.click()

    def get_go_to_alerts(self):
        return self.__go_to_alerts

    def get_alert_button(self):
        return self.__alert_button
