from models.frame_test_data import FrameTestData
from pages.frame_page import FramePage
from pages.left_menu import LeftMenu
from pages.main_page import MainPage
from pages.nested_frame_page import NestedFramePage


def test_frame():
    main_page = MainPage()
    nested_frame_page = NestedFramePage()
    left_menu = LeftMenu()
    frame_page = FramePage()
    test_data = FrameTestData.load_from_json()
    assert main_page.is_displayed(), "Main page is not displayed"
    main_page.go_to_alerts_window()

    assert left_menu.is_displayed(), "Left menu is not displayed"
    left_menu.go_to_nested_frames()

    assert nested_frame_page.is_displayed(), "Nested frame page is not displayed"
    assert nested_frame_page.get_parent_text() == test_data.parent_text, 'Parent text is incorrrect'
    assert nested_frame_page.get_child_text() == test_data.child_text, 'Child text is incorrect'

    left_menu.go_to_frames()
    assert frame_page.get_upper_frame_text() == frame_page.get_upper_frame_text() == test_data.sample_text, 'The text in frames is not the same'
