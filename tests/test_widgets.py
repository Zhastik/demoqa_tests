from pages.widgets.auto_complete import AutoComplete
from pages.widgets.date_picker import DatePicker
from pages.widgets.progress_bar import ProgressBar
from pages.widgets.tool_tips import ToolTips
from pages.widgets.select_menu import SelectMenu


def test_auto_complete_multiple(page):
    auto_complete_page = AutoComplete(page)

    auto_complete_page.navigate()
    auto_complete_page.select_multiple_colors(["Red", "Blue", "Green"])

    auto_complete_page.check_colors_selected(["Red", "Blue", "Green"])

def test_auto_complete_single(page):
    auto_complete_page = AutoComplete(page)

    auto_complete_page.navigate()
    auto_complete_page.select_single_color("Red")

    auto_complete_page.check_color_selected("Red")

def test_select_date(page):
    date_picker_page = DatePicker(page)

    date_picker_page.navigate()
    date_picker_page.select_date("07/15/2026")

    date_picker_page.check_selected_date("07/15/2026")

def test_select_date_and_time(page):
    date_picker_page = DatePicker(page)

    date_picker_page.navigate()
    date_picker_page.select_date_and_time("July 15, 2026 10:30 AM")

    date_picker_page.check_selected_date_and_time("July 15, 2026 10:30 AM")

def test_progress_bar_full(page):
    progress_bar_page = ProgressBar(page)

    progress_bar_page.navigate()
    progress_bar_page.start_progress()

    progress_bar_page.wait_until_progress_is_full()
    progress_bar_page.check_progress_value("100")

def test_progress_bar_reset(page):
    progress_bar_page = ProgressBar(page)

    progress_bar_page.navigate()
    progress_bar_page.start_progress()

    progress_bar_page.wait_until_progress_is_full()
    progress_bar_page.reset_progress()

    progress_bar_page.check_progress_value("0")

def test_progress_bar_stop(page):
    progress_bar_page = ProgressBar(page)

    progress_bar_page.navigate()
    progress_bar_page.start_progress()

    page.wait_for_timeout(1000)

    progress_bar_page.stop_progress()

    value = progress_bar_page.get_progress_value()

    assert value > 0
    assert value < 100

def test_button_tooltip(page):
    tool_tips_page = ToolTips(page)

    tool_tips_page.navigate()
    tool_tips_page.hover_over_button()

    tool_tips_page.check_tooltip_text("You hovered over the Button")

def test_input_tooltip(page):
    tool_tips_page = ToolTips(page)

    tool_tips_page.navigate()
    tool_tips_page.hover_over_input()

    tool_tips_page.check_tooltip_text("You hovered over the text field")

def test_contrary_link_tooltip(page):
    tool_tips_page = ToolTips(page)

    tool_tips_page.navigate()
    tool_tips_page.hover_over_contrary_link()

    tool_tips_page.check_tooltip_text("You hovered over the Contrary")

def test_select_value(page):
    select_menu_page = SelectMenu(page)

    select_menu_page.navigate()
    select_menu_page.select_value("Group 1, option 1")

    select_menu_page.check_text_visible("Group 1, option 1")

def test_select_one(page):
    select_menu_page = SelectMenu(page)

    select_menu_page.navigate()
    select_menu_page.select_one("Mr.")

    select_menu_page.check_text_visible("Mr.")

def test_old_style_select_menu(page):
    select_menu_page = SelectMenu(page)

    select_menu_page.navigate()
    select_menu_page.select_old_style_menu("Blue")

    select_menu_page.check_old_style_value("1")

