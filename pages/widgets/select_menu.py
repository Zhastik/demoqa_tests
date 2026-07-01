from playwright.sync_api import Page, expect


class SelectMenu:
    def __init__(self, page: Page):
        self.page = page

        self.select_value_input = page.get_by_role("combobox").nth(0)
        self.select_one_input = page.get_by_role("combobox").nth(1)

        self.old_style_select = page.get_by_role("combobox").nth(2)

        self.multi_select_input = page.get_by_role("combobox").nth(3)

        self.standard_multi_select = page.get_by_role("listbox")

    def navigate(self):
        self.page.goto("https://demoqa.com/select-menu")

    def select_value(self, value: str):
        self.select_value_input.fill(value)
        self.select_value_input.press("Enter")

    def select_one(self, value: str):
        self.select_one_input.fill(value)
        self.select_one_input.press("Enter")

    def select_old_style_menu(self, color: str):
        self.old_style_select.select_option(label=color)

    def select_multi_colors(self, colors: list[str]):
        for color in colors:
            self.multi_select_input.fill(color)
            self.multi_select_input.press("Enter")

    def select_standard_multi(self, values: list[str]):
        self.standard_multi_select.select_option(values)

    def check_text_visible(self, text: str):
        expect(self.page.get_by_text(text, exact=True)).to_be_visible()

    def check_old_style_value(self, value: str):
        expect(self.old_style_select).to_have_value(value)