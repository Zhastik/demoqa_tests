from playwright.sync_api import Page, expect


class Alerts:
    def __init__(self, page: Page):
        self.page = page

        self.alert_button = page.get_by_role("button", name="Click me").nth(0)
        self.timer_alert_button = page.get_by_role("button", name="Click me").nth(1)
        self.confirm_button = page.get_by_role("button", name="Click me").nth(2)
        self.prompt_button = page.get_by_role("button", name="Click me").nth(3)

        self.confirm_result = page.get_by_text("You selected")
        self.prompt_result = page.get_by_text("You entered")

        self.dialog_message = None

    def navigate(self):
        self.page.goto("https://demoqa.com/alerts")

    def dialog_accept(self, dialog):
        self.dialog_message = dialog.message
        dialog.accept()

    def dialog_dismiss(self, dialog):
        self.dialog_message = dialog.message
        dialog.dismiss()

    def dialog_prompt_accept(self, dialog, text: str):
        self.dialog_message = dialog.message
        dialog.accept(text)

    def click_alert_button(self):
        self.dialog_message = None

        self.page.once("dialog", self.dialog_accept)
        self.alert_button.click()

        return self.dialog_message

    def click_timer_alert_button(self):
        self.dialog_message = None

        self.page.once("dialog", self.dialog_accept)
        self.timer_alert_button.click()

        self.page.wait_for_timeout(6000)

        return self.dialog_message

    def accept_confirm(self):
        self.dialog_message = None

        self.page.once("dialog", self.dialog_accept)
        self.confirm_button.click()

        return self.dialog_message

    def dismiss_confirm(self):
        self.dialog_message = None

        self.page.once("dialog", self.dialog_dismiss)
        self.confirm_button.click()

        return self.dialog_message

    def fill_prompt(self, text: str):
        self.dialog_message = None

        self.page.once(
            "dialog",
            lambda dialog: self.dialog_prompt_accept(dialog, text)
        )

        self.prompt_button.click()

        return self.dialog_message

    def check_confirm_result(self, result: str):
        expect(self.confirm_result).to_have_text(f"You selected {result}")

    def check_prompt_result(self, text: str):
        expect(self.prompt_result).to_have_text(f"You entered {text}")