from selenium.webdriver.support.wait import WebDriverWait

from config.config_manager import ConfigManager
from config.logger import Logger
from core.driver import Driver
from selenium.webdriver.common.alert import Alert


class BrowserManager:
    @staticmethod
    def switch_to_alert():
        Logger.info('Switching to an alert')
        return Alert(Driver().driver)

    @staticmethod
    def accept_alert():
        Logger.info('Switching to an alert and accepting it')
        BrowserManager.switch_to_alert().accept()

    @staticmethod
    def dismiss_alert():
        Logger.info('Switching to an alert and dismissing it')
        BrowserManager.switch_to_alert().dismiss()

    @staticmethod
    def get_alert_text():
        Logger.info('Switching to an alert and getting text of it')
        return BrowserManager.switch_to_alert().text

    @staticmethod
    def send_keys_alert(text):
        Logger.info('Switching to an alert and sending keys to it')
        return BrowserManager.switch_to_alert().send_keys(text)

    @staticmethod
    def get_old_tabs():
        Logger.info('Getting a set of browser tabs')
        return set(Driver().driver.window_handles)

    @staticmethod
    def get_new_tab_id(old_tabs):
        Logger.info('Getting an ID of a new browser tab')
        WebDriverWait(Driver().driver, ConfigManager.get('waiting_time')).until(lambda d: len(d.window_handles) > len(old_tabs))
        return (set(Driver().driver.window_handles) - old_tabs).pop()

    @staticmethod
    def switch_to_tab(index):
        Logger.info('Switching to a browser tab by the index')
        window_handles = Driver().driver.window_handles
        for handle in window_handles:
            if handle == index:
                Driver().driver.switch_to.window(handle)
                break

    @staticmethod
    def close_current_tab():
        Logger.info('Closing current browser tab')
        Driver().driver.close()
        Driver().driver.switch_to.window(Driver().driver.window_handles[-1])

    @staticmethod
    def get_current_url():
        Logger.info('Getting current url')
        return Driver().driver.current_url
