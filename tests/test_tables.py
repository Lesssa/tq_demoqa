import pytest

from models.user import User
from pages.header import Header
from pages.left_menu import LeftMenu
from pages.main_page import MainPage
from pages.web_tables_page import WebTablesPage


@pytest.mark.parametrize("user_data", User.load_all())
def test_tables(user_data):
    main_page = MainPage()
    left_menu = LeftMenu()
    web_tables_page = WebTablesPage()
    header = Header()

    assert main_page.is_displayed(), "Main page is not displayed"
    main_page.go_to_elements()

    assert left_menu.is_displayed(), "Left menu is not displayed"
    left_menu.go_to_web_tables()

    assert web_tables_page.is_displayed(), "Web tables page s not displayed"
    web_tables_page.get_add_button().click()
    web_tables_page.wait_reg_form_displayed()

    for field, value in user_data.dict(by_alias=True).items():
        web_tables_page.send_keys(field, str(value))

    web_tables_page.click_submit_button()
    assert user_data in web_tables_page.get_users(), "Inserted user is not in the table"

    web_tables_page.delete_row(len(web_tables_page.get_users()))

    assert user_data not in web_tables_page.get_users(), "User was not deleted"

    header.go_to_home()
    assert main_page.is_displayed(), "Main page is not displayed"
