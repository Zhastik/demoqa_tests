from playwright.sync_api import Page, expect


class AutoComplete:
    def __init__(self, page: Page):
        self.page = page

        self.multiple_color_input = page.get_by_role("combobox").nth(0)
        self.single_color_input = page.get_by_role("combobox").nth(1)

    def navigate(self):
        self.page.goto("https://demoqa.com/auto-complete")

    def select_multiple_colors(self, colors: list[str]):
        for color in colors:
            self.multiple_color_input.fill(color)
            self.multiple_color_input.press("Enter")

    def select_single_color(self, color: str):
        self.single_color_input.fill(color)
        self.single_color_input.press("Enter")

    def check_color_selected(self, color: str):
        expect(self.page.get_by_text(color, exact=True)).to_be_visible()

    def check_colors_selected(self, colors: list[str]):
        for color in colors:
            expect(self.page.get_by_text(color, exact=True)).to_be_visible()