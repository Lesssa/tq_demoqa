from selenium.webdriver.common.by import By

from config.logger import Logger
from elements.button import Button
from elements.label import Label
from pages.base_form import BaseForm


class AlertsPage(BaseForm):
    __alerts_block = Label((By.XPATH, '//*[@id="javascriptAlertsWrapper"]'), "Alerts block")
    __alert_button = Button((By.XPATH, '//button[@id="alertButton"]'), 'Alert button')
    __confirm_button = Button((By.XPATH, '//*[@id="confirmButton"]'), 'Confirm box button')
    __prompt_button = Button((By.XPATH, '//*[@id="promtButton"]'), 'Prompt box button')
    __confirm_result = Label((By.XPATH, '//*[@id="confirmResult"]'), 'Confirm results block')
    __prompt_result = Label((By.XPATH, '//*[@id="promptResult"]'), 'Prompt results block')

    def __init__(self):
        super().__init__(self.__alerts_block, 'Alerts Page')

    def click_alert_button(self):
        Logger.info('Clicking the button for calling an alert')
        self.__alert_button .click()

    def click_confirm_button(self):
        Logger.info('Clicking the button for calling a confirm box')
        self.__confirm_button.click()

    def click_prompt_button(self):
        Logger.info('Clicking the button for calling a prompt box')
        self.__prompt_button.click()

    def get_confirm_result(self):
        Logger.info('Getting a confirm box result')
        return self.__confirm_result.get_text()

    def get_prompt_result(self):
        Logger.info('Getting a prompt box result')
        return self.__prompt_result.get_text()
