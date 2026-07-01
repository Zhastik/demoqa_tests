from playwright.sync_api import expect


class RadioButton:
    def __init__(self, page):
        self.page = page

        self.yes_radio = page.locator("#yesRadio")
        self.impressive_radio = page.locator("#impressiveRadio")
        self.no_radio = page.locator("#noRadio")

        self.result = page.locator(".text-success")

    def navigate(self):
        self.page.goto("https://demoqa.com/radio-button")

    def click_yes(self):
        self.yes_radio.click()

    def click_impressive(self):
        self.impressive_radio.click()

    def check_yes_selected(self):
        expect(self.yes_radio).to_be_checked()
        expect(self.result).to_have_text("Yes")

    def check_impressive_selected(self):
        expect(self.impressive_radio).to_be_checked()
        expect(self.result).to_have_text("Impressive")

    def check_no_disabled(self):
        expect(self.no_radio).to_be_disabled()