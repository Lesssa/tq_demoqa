from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config_manager import ConfigManager
from config.logger import setup_logger
from core.driver import Driver
from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from pages.base_form import BaseForm
logger = setup_logger('WebTablesPage')


class WebTablesPage(BaseForm):
    __web_tables_block = (By.XPATH, '//*[@class="web-tables-wrapper"]')
    __add_button = Button((By.XPATH, '//button[@id="addNewRecordButton"]'), 'Add button')
    __registration_form = (By.XPATH, '//*[@class="fade modal-backdrop show"]')
    __inputs_xpath = '//input[@id='
    __submit_button = Button((By.XPATH, '//button[@id="submit"]'), 'Submit button')
    __table = BaseElement((By.XPATH, '//*[@class="rt-table"]'), 'Table')
    __table_rows = (By.XPATH, '//*[@class="rt-tr-group"]')
    __table_cells = (By.XPATH, './/*[@class="rt-td"]')
    __delete_button = '//*[@id="delete-record-'
    __column_names = (By.XPATH, '//*[@class="rt-resizable-header-content"]')

    def __init__(self):
        logger.info('Initiating Web tables page')
        super().__init__(self.__web_tables_block, 'Web Tables Page')

    def get_add_button(self):
        logger.info('Getting a button for adding a new user')
        return self.__add_button

    def wait_reg_form_displayed(self):
        logger.info('Waiting for presence of registration form to be located')
        return WebDriverWait(Driver().get_driver, ConfigManager.get('waiting_time')).until(
            EC.presence_of_element_located(self.__registration_form)
        )

    def send_keys(self, id, value):
        logger.info('Sending keys to a registration form field')
        xpath = self.__inputs_xpath + '"' + id + '"' + ']'
        element = Input((By.XPATH, xpath), f'Ввод в поле c id {id}')
        element.send_keys(value)

    def get_submit_button(self):
        logger.info('Getting a button for submitting sending of the registration form')
        return self.__submit_button

    def get_all_rows(self):
        logger.info('Getting all rows from a table')
        rows = Driver().get_driver.find_elements(*self.__table_rows)
        return rows

    def get_not_empty_rows(self):
        logger.info('Getting not empty rows from a table')
        rows = self.get_all_rows()
        not_empty_rows = [row for row in rows if row.text.strip() != '']
        return not_empty_rows

    def get_values_from_last_row(self):
        logger.info('Getting values in list from last row')
        not_empty = self.get_not_empty_rows()
        return [str(cell.text).strip() for cell in not_empty[-1].find_elements(*self.__table_cells)]

    def get_column_names(self):
        logger.info('Getting column names of a table')
        return [header.text.strip() for header in Driver().get_driver.find_elements(*self.__column_names)]

    def delete_row(self, index):
        logger.info('Deleting a row by an index')
        Button((By.XPATH, self.__delete_button + str(index) + '"]'), 'Delete button').click()
