from playwright.sync_api import expect


class CheckBox:
    def __init__(self, page):
        self.page = page
        self.result = page.locator("#result")
        self.expand_all_button = page.locator("button[title='Expand all']")

    def navigate(self):
        self.page.goto("https://demoqa.com/checkbox")

    def expand_all(self):
        self.expand_all_button.click()

    def checkbox_by_name(self, name):
        return self.page.get_by_role("checkbox", name=f"Select {name}")

    def select_checkbox(self, name):
        self.checkbox_by_name(name).click()

    def should_be_checked(self, name):
        expect(self.checkbox_by_name(name)).to_have_attribute("aria-checked", "true")

    def should_result_contain(self, value):
        expect(self.result).to_contain_text(value)