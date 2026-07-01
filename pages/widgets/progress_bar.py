from playwright.sync_api import Page, expect


class ProgressBar:
    def __init__(self, page: Page):
        self.page = page

        self.progress_bar = page.get_by_role("progressbar")
        self.start_button = page.get_by_role("button", name="Start")
        self.stop_button = page.get_by_role("button", name="Stop")
        self.reset_button = page.get_by_role("button", name="Reset")

    def navigate(self):
        self.page.goto("https://demoqa.com/progress-bar")

    def start_progress(self):
        self.start_button.click()

    def stop_progress(self):
        self.stop_button.click()

    def reset_progress(self):
        self.reset_button.click()

    def wait_until_progress_is_full(self):
        expect(self.progress_bar).to_have_text("100%", timeout=15000)

    def check_progress_value(self, value: str):
        expect(self.progress_bar).to_have_text(f"{value}%")

    def get_progress_value(self):
        value = self.progress_bar.get_attribute("aria-valuenow")
        return int(value)