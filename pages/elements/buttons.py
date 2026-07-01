from playwright.sync_api import expect


class Buttons:
    def __init__(self, page):
        self.page = page

        self.double_click_btn = page.locator("#doubleClickBtn")
        self.right_click_btn = page.locator("#rightClickBtn")
        self.click_me_btn = page.get_by_role("button", name="Click Me", exact=True)

        self.double_click_message = page.locator("#doubleClickMessage")
        self.right_click_message = page.locator("#rightClickMessage")
        self.dynamic_click_message = page.locator("#dynamicClickMessage")

    def navigate(self):
        self.page.goto("https://demoqa.com/buttons")

    def double_click(self):
        self.double_click_btn.dblclick()

    def right_click(self):
        self.right_click_btn.click(button="right")

    def click_me(self):
        self.click_me_btn.click()

    def check_double_click_message(self):
        expect(self.double_click_message).to_have_text("You have done a double click")

    def check_right_click_message(self):
        expect(self.right_click_message).to_have_text("You have done a right click")

    def check_dynamic_click_message(self):
        expect(self.dynamic_click_message).to_have_text("You have done a dynamic click")