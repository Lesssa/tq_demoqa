from pages.alert import Alert
from pages.alerts_page import AlertsPage
from pages.main_page import MainPage


def test_about():
    main_page = MainPage()
    main_page.is_displayed()
    main_page.go_to_alerts_window()

    alerts_page = AlertsPage()
    alerts_page.is_displayed()
    alerts_page.get_go_to_alerts().click()
    alerts_page.get_alert_button().click()
    alert = Alert()
    alert.accept()



