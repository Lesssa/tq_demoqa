from core.browser_manager import BrowserManager
from models.alert_test_data import AlertTestData
from pages.alerts_page import AlertsPage
from pages.left_menu import LeftMenu
from pages.main_page import MainPage


def test_alert():
    main_page = MainPage()
    left_menu = LeftMenu()
    alerts_page = AlertsPage()
    test_data = AlertTestData.load_from_json()
    assert main_page.is_displayed(), "Main page is not displayed"
    main_page.go_to_alerts_window()

    assert left_menu.is_displayed(), "Left menu is not displayed"
    left_menu.go_to_alerts()

    assert alerts_page.is_displayed(), "Alert page is not displayed"
    alerts_page.click_alert_button()
    assert BrowserManager.get_alert_text() == test_data.alert_text, "Alert text is incorrect"
    BrowserManager.accept_alert()

    alerts_page.click_confirm_button()
    assert BrowserManager.get_alert_text() == test_data.confirm_alert_text, "Confirm box text is incorrect"
    BrowserManager.accept_alert()
    assert alerts_page.get_confirm_result() == test_data.after_confirm_text, "Confirm results are incorrect"

    alerts_page.click_prompt_button()
    assert BrowserManager.get_alert_text() == test_data.prompt_alert_text, "Prompt box text is incorrect"
    BrowserManager.send_keys_alert(test_data.name_to_prompt)
    BrowserManager.accept_alert()
    assert alerts_page.get_prompt_result() == test_data.after_prompt_text + test_data.name_to_prompt, "Confirm results are incorrect"
