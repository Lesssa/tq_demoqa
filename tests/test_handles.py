from core.browser_manager import BrowserManager
from pages.browser_page import BrowserPage
from pages.left_menu import LeftMenu
from pages.link_page import LinkPage
from pages.main_page import MainPage


def test_handles():
    main_page = MainPage()
    left_menu = LeftMenu()
    browser_page = BrowserPage()
    link_page = LinkPage()
    assert main_page.is_displayed(), "Main page is not displayed"
    main_page.go_to_alerts_window()

    assert left_menu.is_displayed(), "Left menu is not displayed"
    left_menu.go_to_browser_windows()

    assert browser_page.is_displayed(), "Browser page is not displayed"
    old_tabs = BrowserManager.get_old_tabs()
    browser_page.click_new_tab_button()
    BrowserManager.switch_to_tab(BrowserManager.get_new_tab_id(old_tabs))
    # todo need to check is_displayed for opened page
    assert BrowserManager.get_current_url() == 'https://demoqa.com/sample', 'New tab URL is incorrect'
    BrowserManager.close_current_tab()
    BrowserManager.switch_to_tab(old_tabs.pop())
    assert browser_page.is_displayed(), "Browser page is not displayed"

    left_menu.open_elements_list()
    left_menu.wait_shown_list()
    left_menu.go_to_links()
    assert link_page.is_displayed(), "Link page is not displayed"
    old_tabs = BrowserManager.get_old_tabs()
    link_page.get_home_link().click()
    BrowserManager.switch_to_tab(BrowserManager.get_new_tab_id(old_tabs))
    assert main_page.is_displayed(), "Main page is not displayed"
    assert BrowserManager.get_current_url() == 'https://demoqa.com/', 'New tab URL is incorrect'
    BrowserManager.switch_to_tab(old_tabs.pop())
    assert link_page.is_displayed(), "Link page is not displayed"
