from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.driver import Driver


class BaseElement:
    def __init__(self, locator, name):
        self.locator = locator
        self.name = name

    def find(self):
        print(self.locator)
        return WebDriverWait(Driver().get_driver, 10).until(
            EC.presence_of_element_located(self.locator)
        )

    def click(self):
        self.find().click()

    def get_text(self):
        return self.find().text

    def send_keys(self, text):
        self.find().send_keys(text)

    def is_displayed(self):
        try:
            element = self.find()
            return element.is_displayed()
        except:
            return False

    # def move_to(self):
    #     element = self.find()
    #     action = ActionChains(Driver().get_driver)
    #     action.move_to_element(element).perform()
