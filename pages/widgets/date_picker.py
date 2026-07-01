from playwright.sync_api import Page, expect


class DatePicker:
    def __init__(self, page: Page):
        self.page = page

        self.select_date_input = page.get_by_role("textbox").nth(0)
        self.date_and_time_input = page.get_by_role("textbox").nth(1)

    def navigate(self):
        self.page.goto("https://demoqa.com/date-picker")

    def select_date(self, date: str):
        self.select_date_input.click()
        self.select_date_input.press("Control+A")
        self.select_date_input.fill(date)
        self.select_date_input.press("Enter")

    def select_date_and_time(self, date_time: str):
        self.date_and_time_input.click()
        self.date_and_time_input.press("Control+A")
        self.date_and_time_input.fill(date_time)
        self.date_and_time_input.press("Enter")

    def check_selected_date(self, date: str):
        expect(self.select_date_input).to_have_value(date)

    def check_selected_date_and_time(self, date_time: str):
        expect(self.date_and_time_input).to_have_value(date_time)