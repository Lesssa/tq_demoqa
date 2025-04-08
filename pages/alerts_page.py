from selenium.webdriver.common.by import By

from config.logger import Logger
from elements.base_element import BaseElement
from elements.button import Button
from pages.base_form import BaseForm
logger = Logger.get_logger()

# todo remove base element
class AlertsPage(BaseForm):
    __alerts_block = (By.XPATH, '//*[@id="javascriptAlertsWrapper"]')
    __alert_button = Button((By.XPATH, '//button[@id="alertButton"]'), 'Alert button')
    __confirm_button = Button((By.XPATH, '//*[@id="confirmButton"]'), 'Confirm box button')
    __prompt_button = Button((By.XPATH, '//*[@id="promtButton"]'), 'Prompt box button')
    __confirm_result = BaseElement((By.XPATH, '//*[@id="confirmResult"]'), 'Confirm results block')
    __prompt_result = BaseElement((By.XPATH, '//*[@id="promptResult"]'), 'Prompt results block')

    def __init__(self):
        super().__init__(self.__alerts_block, 'Alerts Page')

    def click_alert_button(self):
        logger.info('Clicking the button for calling an alert')
        self.__alert_button .click()

    def click_confirm_button(self):
        logger.info('Clicking the button for calling a confirm box')
        self.__confirm_button.click()

    def click_prompt_button(self):
        logger.info('Clicking the button for calling a prompt box')
        self.__prompt_button.click()

# todo redo getters
    def get_confirm_result(self):
        logger.info('Getting a confirm box result element')
        return self.__confirm_result

    def get_prompt_result(self):
        logger.info('Getting a prompt box result element')
        return self.__prompt_result
