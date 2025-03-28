from selenium.webdriver.common.alert import Alert as SeleniumAlert
from core.driver import Driver


class Alert:
    @property
    def alert(self):
        return SeleniumAlert(Driver().get_driver)

    def accept(self):
        self.alert.accept()

    def dismiss(self):
        self.alert.dismiss()

    def get_text(self):
        return self.alert.text

    def send_keys(self, text):
        self.alert.send_keys(text)
