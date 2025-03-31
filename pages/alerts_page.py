from selenium.webdriver.common.by import By

from config.logger import setup_logger
from elements.base_element import BaseElement
from elements.button import Button
from pages.base_form import BaseForm
logger = setup_logger('AlertsPage')

class AlertsPage(BaseForm):
    __alerts_block = (By.XPATH, '//*[@id="javascriptAlertsWrapper"]')
    __alert_button = Button((By.XPATH, '//button[@id="alertButton"]'), 'Alert button')
    __confirm_button = Button((By.XPATH, '//*[@id="confirmButton"]'), 'Confirm box button')
    __prompt_button = Button((By.XPATH, '//*[@id="promtButton"]'), 'Prompt box button')
    __confirm_result = BaseElement((By.XPATH, '//*[@id="confirmResult"]'), 'Confirm results block')
    __prompt_result = BaseElement((By.XPATH, '//*[@id="promptResult"]'), 'Prompt results block')

    def __init__(self):
        logger.info('Initiating an alert page')
        super().__init__(self.__alerts_block, 'Alerts Page')

    def get_alert_button(self):
        logger.info('Getting the button for calling an alert')
        return self.__alert_button

    def get_confirm_button(self):
        logger.info('Getting the button for calling a confirm box')
        return self.__confirm_button

    def get_prompt_button(self):
        logger.info('Getting the button for calling a prompt box')
        return self.__prompt_button

    def get_confirm_result(self):
        logger.info('Getting a confirm box result element')
        return self.__confirm_result

    def get_prompt_result(self):
        logger.info('Getting a prompt box result element')
        return self.__prompt_result
