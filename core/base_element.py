from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser import Browser


class BaseElement:
    def __init__(self, locator):
        self.locator = locator
        self.driver = Browser.get_driver()

    def find(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator)
        )

    def click(self):
        self.find().click()

    def get_text(self):
        return self.find().text

    def send_keys(self, text):
        self.find().send_keys(text)
