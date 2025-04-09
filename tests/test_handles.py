from core.browser_manager import BrowserManager
from pages.browser_page import BrowserPage
from pages.left_menu import LeftMenu
from pages.link_page import LinkPage
from pages.main_page import MainPage
from pages.sample_page import SamplePage


def test_handles():
    main_page = MainPage()
    left_menu = LeftMenu()
    browser_page = BrowserPage()
    link_page = LinkPage()
    sample_page = SamplePage()
    assert main_page.is_displayed(), "Main page is not displayed"
    main_page.go_to_alerts_window()

    assert left_menu.is_displayed(), "Left menu is not displayed"
    left_menu.go_to_browser_windows()

    assert browser_page.is_displayed(), "Browser page is not displayed"
    old_tabs = BrowserManager.get_old_tabs()
    browser_page.click_new_tab_button()
    BrowserManager.switch_to_tab(BrowserManager.get_new_tab_id(old_tabs))
    assert sample_page.is_displayed(), "New tab is not displayed"
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
    BrowserManager.switch_to_tab(old_tabs.pop())
    assert link_page.is_displayed(), "Link page is not displayed"
