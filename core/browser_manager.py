from selenium.webdriver.support.wait import WebDriverWait

from config.config_manager import ConfigManager
from config.logger import setup_logger
from core.driver import Driver
from selenium.webdriver.common.alert import Alert
logger = setup_logger('BrowserManager')


class BrowserManager:
    @staticmethod
    def switch_to_alert():
        logger.info('Switching to an alert')
        return Alert(Driver().get_driver)

    @staticmethod
    def accept_alert():
        logger.info('Switching to an alert and accepting it')
        BrowserManager.switch_to_alert().accept()

    @staticmethod
    def dismiss_alert():
        logger.info('Switching to an alert and dismissing it')
        BrowserManager.switch_to_alert().dismiss()

    @staticmethod
    def get_alert_text():
        logger.info('Switching to an alert and getting text of it')
        return BrowserManager.switch_to_alert().text

    @staticmethod
    def send_keys_alert(text):
        logger.info('Switching to an alert and sending keys to it')
        return BrowserManager.switch_to_alert().send_keys(text)

    @staticmethod
    def get_old_tabs():
        logger.info('Getting a set of browser tabs')
        return set(Driver().get_driver.window_handles)

    @staticmethod
    def get_new_tab_id(old_tabs):
        logger.info('Getting an ID of a new browser tab')
        WebDriverWait(Driver().get_driver, ConfigManager.get('waiting_time')).until(lambda d: len(d.window_handles) > len(old_tabs))
        return (set(Driver().get_driver.window_handles) - old_tabs).pop()

    @staticmethod
    def switch_to_tab(index):
        logger.info('Switching to a browser tab by the index')
        window_handles = Driver().get_driver.window_handles
        for handle in window_handles:
            if handle == index:
                Driver().get_driver.switch_to.window(handle)
                break

    @staticmethod
    def close_current_tab():
        logger.info('Closing current browser tab')
        Driver().get_driver.close()
        Driver().get_driver.switch_to.window(Driver().get_driver.window_handles[-1])

    @staticmethod
    def get_current_url():
        logger.info('Getting current url')
        return Driver().get_driver.current_url
