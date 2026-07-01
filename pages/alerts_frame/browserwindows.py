from playwright.sync_api import Page, expect


class BrowserWindows:
    def __init__(self, page: Page):
        self.page = page

        self.new_tab_button = page.get_by_role("button", name="New Tab")
        self.new_window_button = page.get_by_role("button", name="New Window", exact=True)
        self.new_window_message_button = page.get_by_role("button", name="New Window Message")

    def navigate(self):
        self.page.goto("https://demoqa.com/browser-windows")

    def open_new_tab(self):
        with self.page.context.expect_page() as new_page_info:
            self.new_tab_button.click()

        new_page = new_page_info.value
        new_page.wait_for_load_state()
        return new_page

    def open_new_window(self):
        with self.page.context.expect_page() as new_page_info:
            self.new_window_button.click()

        new_page = new_page_info.value
        new_page.wait_for_load_state()
        return new_page

    def open_new_window_message(self):
        with self.page.context.expect_page() as new_page_info:
            self.new_window_message_button.click()

        new_page = new_page_info.value
        new_page.wait_for_load_state()
        return new_page