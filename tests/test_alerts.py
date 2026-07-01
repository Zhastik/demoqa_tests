from pages.alerts_frame.browserwindows import BrowserWindows
from playwright.sync_api import expect
from pages.alerts_frame.alerts import Alerts


def test_new_tab(page):
    browser_windows_page = BrowserWindows(page)

    browser_windows_page.navigate()
    new_page = browser_windows_page.open_new_tab()

    expect(new_page.get_by_text("This is a sample page")).to_be_visible()

    new_page.close()

def test_new_window(page):
    browser_windows_page = BrowserWindows(page)

    browser_windows_page.navigate()
    new_page = browser_windows_page.open_new_window()

    expect(new_page.get_by_text("This is a sample page")).to_be_visible()

    new_page.close()

def test_alert(page):
    alerts_page = Alerts(page)

    alerts_page.navigate()
    message = alerts_page.click_alert_button()

    assert message == "You clicked a button"

def test_timer_alert(page):
    alerts_page = Alerts(page)

    alerts_page.navigate()
    message = alerts_page.click_timer_alert_button()

    assert message == "This alert appeared after 5 seconds"

def test_confirm_accept(page):
    alerts_page = Alerts(page)

    alerts_page.navigate()
    message = alerts_page.accept_confirm()

    assert message == "Do you confirm action?"

    alerts_page.check_confirm_result("Ok")

def test_confirm_dismiss(page):
    alerts_page = Alerts(page)

    alerts_page.navigate()
    message = alerts_page.dismiss_confirm()

    assert message == "Do you confirm action?"

    alerts_page.check_confirm_result("Cancel")

def test_prompt(page):
    alerts_page = Alerts(page)

    alerts_page.navigate()
    message = alerts_page.fill_prompt("Jes")

    assert message == "Please enter your name"

    alerts_page.check_prompt_result("Jes")