from pages.base_form import BaseForm
from elements.button import Button


class MainPage(BaseForm):
    __home_banner = '//*[@class="home-banner"]'
    __alerts_button = Button('//*[text()="Alerts, Frame & Windows"]')

    def __init__(self):
        super().__init__(MainPage.__home_banner, "Alerts Page")

    def go_to_alerts(self):
        self.__alerts_button.click()
