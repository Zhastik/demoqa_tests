from playwright.sync_api import Page, expect


class TextBox():
    def __init__(self, page: Page):
        self.page = page
        self.name_input = page.locator("#userName")
        self.email_input = page.get_by_placeholder("name@example.com")
        self.current_address = page.locator(".form-control").nth(2)
        self.permanent_address = page.locator("#permanentAddress")
        self.result_name = page.locator("#name")
        self.result_email = page.locator("#email")
        self.result_currentaddr = page.locator(".mb-1").nth(2)
        self.result_permananetaddr = page.locator(".mb-1").last
        self.submit_button = page.get_by_role("button", name="Submit")

    def navigate(self):
        self.page.goto("https://demoqa.com/text-box")

    def login_poz(self, name: str, email: str, current: str, permanent: str):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.current_address.fill(current)
        self.permanent_address.fill(permanent)
        self.submit_button.click()

    def get_result_massege(self):
        result = []
        result.append(self.result_name.inner_text())
        result.append(self.result_email.inner_text())
        result.append(self.result_currentaddr.inner_text())
        result.append(self.result_permananetaddr.inner_text())
        return result

