from pages.alerts_page import Alerts
from pages.main_page import MainPage


def test_about():
    main_page = MainPage()
    main_page.is_displayed()
    main_page.go_to_alerts()

    alerts = Alerts()
    alerts.is_displayed()



