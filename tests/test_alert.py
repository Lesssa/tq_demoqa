from core.browser_manager import BrowserManager
from pages.alerts_page import AlertsPage
from pages.left_menu import LeftMenu
from pages.main_page import MainPage


def test_alert():
    main_page = MainPage()
    left_menu = LeftMenu()
    alerts_page = AlertsPage()
    assert main_page.is_displayed(), "Main page is not displayed"
    main_page.go_to_alerts_window()

    assert left_menu.is_displayed(), "Left menu is not displayed"
    left_menu.go_to_alerts()

    assert alerts_page.is_displayed(), "Alert page is not displayed"
    alerts_page.get_alert_button().click()
    assert BrowserManager.get_alert_text() == "You clicked a button", "Alert text is incorrect"
    BrowserManager.accept_alert()
    assert alerts_page.get_alert_button().is_displayed(), "Alert wasn't accepted"

    alerts_page.get_confirm_button().click()
    assert BrowserManager.get_alert_text() == "Do you confirm action?", "Confirm box text is incorrect"
    BrowserManager.accept_alert()
    assert alerts_page.get_alert_button().is_displayed(), "Action wasn't confirmed"
    assert alerts_page.get_confirm_result().get_text() == "You selected Ok", "Confirm results are incorrect"

    alerts_page.get_prompt_button().click()
    assert BrowserManager.get_alert_text() == "Please enter your name", "Prompt box text is incorrect"
    BrowserManager.send_keys_alert('Lisa')
    BrowserManager.accept_alert()
    assert alerts_page.get_alert_button().is_displayed(), "Prompt box didn't close"
    assert alerts_page.get_prompt_result().get_text() == "You entered Lisa", "Confirm results are incorrect"
