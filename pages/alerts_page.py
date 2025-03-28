from selenium.webdriver.common.by import By

from pages.base_form import BaseForm


class Alerts(BaseForm):
    __left_panel = (By.XPATH, '//*[@class="left-pannel"]')
    __showed_alerts_panel = (By.XPATH, '//*[@class="element-group" and .//text()[contains(., "Alerts, Frame & Windows")]]//*[@class="element-list collapse show"]')
    __alerts_button = (By.XPATH, '//*[@id="item-1" and *//text()="Alerts"]')

    def __init__(self):
        super().__init__(self.__showed_alerts_panel, 'Alerts Page')

