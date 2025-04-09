from selenium.webdriver.common.by import By
from config.logger import Logger
from core.driver import Driver
from elements.button import Button
from elements.input import Input
from elements.label import Label
from models.user import User
from pages.base_form import BaseForm


class WebTablesPage(BaseForm):
    __web_tables_block = Label((By.XPATH, '//*[contains(@class, "web-tables-wrapper")]'), 'Web tables block')
    __add_button = Button((By.XPATH, '//button[@id="addNewRecordButton"]'), 'Add button')
    __input_firstname = Input((By.XPATH, '//input[@id="firstName"]'), "First name input")
    __input_lastname = Input((By.XPATH, '//input[@id="lastName"]'), "Last name input")
    __input_email = Input((By.XPATH, '//input[@id="userEmail"]'), "Email input")
    __input_age = Input((By.XPATH, '//input[@id="age"]'), "Age input")
    __input_salary = Input((By.XPATH, '//input[@id="salary"]'), "Salary input")
    __input_department = Input((By.XPATH, '//input[@id="department"]'), "Department input")
    __submit_button = Button((By.XPATH, '//button[@id="submit"]'), 'Submit button')
    __table_rows = (By.XPATH, '//div[contains(@class, "rt-tr-group")][.//div[contains(@class, "rt-td") and text() != ""]]')
    __table_cells = (By.XPATH, './/*[contains(@class, "rt-td")]')
    __delete_button = '//*[@id="delete-record-'
    __column_names = (By.XPATH, '//*[contains(@class, "rt-resizable-header-content")]')

    def __init__(self):
        super().__init__(self.__web_tables_block, 'Web Tables Page')

    def __get_column_names(self):
        Logger.info('Getting column names of a table')
        return [header.text.strip() for header in Driver().driver.find_elements(*self.__column_names)]

    def delete_row_by_user(self, user: User):
        Logger.info(f'Deleting row for user {user.first_name} {user.last_name}')
        users = self.get_users()
        user_index = self.__find_user_index(users, user)
        if user_index is not None:
            self.delete_row(user_index + 1)
        else:
            Logger.error(f"User {user.first_name} {user.last_name} not found.")
            raise Exception(f"User {user.first_name} {user.last_name} not found.")

    @staticmethod
    def __find_user_index(users, target_user: User):
        Logger.info("Finding index of a user")
        for index, user in enumerate(users):
            if (user.first_name == target_user.first_name and
                    user.last_name == target_user.last_name and
                    user.user_email == target_user.user_email and
                    user.age == target_user.age and
                    user.salary == target_user.salary and
                    user.department == target_user.department):
                return index
        return None

    def delete_row(self, index):
        Logger.info('Deleting a row by an index')
        Button((By.XPATH, self.__delete_button + str(index) + '"]'), 'Delete button').click()

    def add_user(self, user):
        Logger.info("Adding user")
        if not self.__add_button.is_displayed():
            Logger.error("Add button is not present")
            raise Exception("Add button is not displayed")
        self.__add_button.click()
        self.__input_firstname.send_keys(user.first_name)
        self.__input_lastname.send_keys(user.last_name)
        self.__input_email.send_keys(user.user_email)
        self.__input_age.send_keys(user.age)
        self.__input_salary.send_keys(user.salary)
        self.__input_department.send_keys(user.department)
        self.__submit_button.click()

    def get_users(self):
        Logger.info('Getting all users from the table')
        users = []
        rows = Driver().driver.find_elements(*self.__table_rows)
        column_names = self.__get_column_names()
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
