import pytest
from pages.left_menu import LeftMenu
from pages.main_page import MainPage
from pages.web_tables_page import WebTablesPage


@pytest.mark.parametrize("user_data", [
    {"firstName": "Jon", "lastName": "Snow", "userEmail": "knownothing@gmail.com", "age": 30, "salary": 3000, "department": "alpha"},
    {"firstName": "Buttercup", "lastName": "Cumbersnatch", "userEmail": "BudapestCandygram@mail.ru", "age": 41, "salary": 2000, "department": "beta"}
])
def test_tables(user_data):
    column_mapping = {
        "firstName": "First Name",
        "lastName": "Last Name",
        "userEmail": "Email",
        "age": "Age",
        "salary": "Salary",
        "department": "Department"
    }
    main_page = MainPage()
    left_menu = LeftMenu()
    web_tables_page = WebTablesPage()
    assert main_page.is_displayed(), "Main page is not displayed"
    main_page.go_to_elements()

    assert left_menu.is_displayed(), "Left menu is not displayed"
    left_menu.go_to_web_tables()

    assert web_tables_page.is_displayed(), "Web tables page s not displayed"
    web_tables_page.get_add_button().click()
    web_tables_page.wait_reg_form_displayed()

    for field, value in user_data.items():
        web_tables_page.send_keys(field, str(value))
    web_tables_page.get_submit_button().click()
    not_empty_rows = web_tables_page.get_not_empty_rows()
    last_row_values = web_tables_page.get_values_from_last_row()
    column_names = web_tables_page.get_column_names()
    row_values = []
    for column in column_names:
        for key, value in column_mapping.items():
            if value == column:
                row_values.append(str(user_data[key]))
                break
    assert last_row_values[:6] == row_values, "Inserted row doesn't match original data"
    web_tables_page.delete_row(len(not_empty_rows))
    a = len(not_empty_rows)
    b = web_tables_page.get_not_empty_rows()
    assert len(web_tables_page.get_not_empty_rows()) == len(not_empty_rows) - 1, "Amount of rows didn't change"
    assert [str(value) for value in user_data.values()] not in web_tables_page.get_not_empty_rows(), "Row wasn't deleted"
    web_tables_page.go_to_home()
    assert main_page.is_displayed(), "Main page is not displayed"
