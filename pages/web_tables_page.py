from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config_manager import ConfigManager
from config.logger import Logger
from core.driver import Driver
from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from elements.label import Label
from models.user import User
from pages.base_form import BaseForm
logger = Logger.get_logger()


# todo remove base element
# todo check classes
class WebTablesPage(BaseForm):
    __web_tables_block = (By.XPATH, '//*[contains(@class, "web-tables-wrapper")]')
    __add_button = Button((By.XPATH, '//button[@id="addNewRecordButton"]'), 'Add button')
    __registration_form = (By.XPATH, '//*[contains(@class, "fade modal-backdrop show")]')
    __inputs_xpath = '//input[@id='
    __submit_button = Button((By.XPATH, '//button[@id="submit"]'), 'Submit button')
    __table = Label((By.XPATH, '//*[contains(@class, "rt-table")]'), 'Table')
    __table_rows = (By.XPATH, '//*[contains(@class, "rt-tr-group")]')
    __table_cells = (By.XPATH, './/*[contains(@class, "rt-td")]')
    __delete_button = '//*[@id="delete-record-'
    __column_names = (By.XPATH, '//*[contains(@class, "rt-resizable-header-content")]')

    def __init__(self):
        super().__init__(self.__web_tables_block, 'Web Tables Page')

    def get_add_button(self):
        logger.info('Getting a button for adding a new user')
        return self.__add_button

    def wait_reg_form_displayed(self):
        logger.info('Waiting for presence of registration form to be located')
        return WebDriverWait(Driver().driver, ConfigManager.get('waiting_time')).until(
            EC.presence_of_element_located(self.__registration_form)
        )

    def send_keys(self, id, value):
        logger.info('Sending keys to a registration form field')
        xpath = self.__inputs_xpath + '"' + id + '"' + ']'
        element = Input((By.XPATH, xpath), f'Ввод в поле c id {id}')
        element.send_keys(value)

    def click_submit_button(self):
        logger.info('Clicking a button for submitting sending of the registration form')
        self.__submit_button.click()

    def __get_all_rows(self):
        logger.info('Getting all rows from a table')
        rows = Driver().driver.find_elements(*self.__table_rows)
        return rows

    def __get_not_empty_rows(self):
        logger.info('Getting not empty rows from a table')
        rows = self.__get_all_rows()
        not_empty_rows = [row for row in rows if row.text.strip() != '']
        return not_empty_rows

    def __get_values_from_last_row(self):
        logger.info('Getting values in list from last row')
        not_empty = self.__get_not_empty_rows()
        return [str(cell.text).strip() for cell in not_empty[-1].find_elements(*self.__table_cells)]

    def get_column_names(self):
        logger.info('Getting column names of a table')
        return [header.text.strip() for header in Driver().driver.find_elements(*self.__column_names)]

    def delete_row(self, index):
        logger.info('Deleting a row by an index')
        Button((By.XPATH, self.__delete_button + str(index) + '"]'), 'Delete button').click()

    def get_users(self):
        logger.info('Getting all users from the table')
        users = []
        rows = self.__get_not_empty_rows()
        column_names = self.get_column_names()
        ui_to_alias = {
            field.title: field.alias
            for field in User.model_fields.values()
            if field.title is not None
        }
        for row in rows:
            cells = row.find_elements(*self.__table_cells)
            user_data = {
                ui_to_alias[column_names[i]]: cells[i].text.strip()
                for i in range(len(column_names))
                if column_names[i] in ui_to_alias
            }
            users.append(User(**user_data))
        return users
