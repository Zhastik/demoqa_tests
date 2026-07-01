from playwright.sync_api import Page, expect


class ToolTips:
    def __init__(self, page: Page):
        self.page = page

        self.hover_button = page.get_by_role("button", name="Hover me to see")
        self.hover_input = page.get_by_placeholder("Hover me to see")
        self.contrary_link = page.get_by_role("link", name="Contrary")
        self.section_link = page.get_by_role("link", name="1.10.32")

        self.tooltip = page.get_by_role("tooltip")

    def navigate(self):
        self.page.goto("https://demoqa.com/tool-tips")

    def hover_over_button(self):
        self.hover_button.scroll_into_view_if_needed()
        self.hover_button.hover(force=True)

    def hover_over_input(self):
        self.hover_input.scroll_into_view_if_needed()
        self.hover_input.hover(force=True)

    def hover_over_contrary_link(self):
        self.contrary_link.scroll_into_view_if_needed()
        self.contrary_link.hover(force=True)

    def hover_over_section_link(self):
        self.section_link.scroll_into_view_if_needed()
        self.section_link.hover(force=True)

    def check_tooltip_text(self, text: str):
        expect(self.tooltip).to_be_visible()
        expect(self.tooltip).to_contain_text(text)