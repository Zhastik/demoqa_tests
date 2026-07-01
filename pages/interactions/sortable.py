from playwright.sync_api import Page, expect


class Sortable:
    def __init__(self, page: Page):
        self.page = page

        self.list_tab = page.get_by_role("tab", name="List")
        self.grid_tab = page.get_by_role("tab", name="Grid")

        self.list_panel = page.get_by_role("tabpanel", name="List")
        self.grid_panel = page.get_by_role("tabpanel", name="Grid")

    def navigate(self):
        self.page.goto("https://demoqa.com/sortable")

    def open_list_tab(self):
        self.list_tab.click()

    def open_grid_tab(self):
        self.grid_tab.click()

    def get_list_item(self, name: str):
        return self.list_panel.get_by_text(name, exact=True)

    def get_grid_item(self, name: str):
        return self.grid_panel.get_by_text(name, exact=True)

    def drag_list_item_to_item(self, source: str, target: str):
        source_item = self.get_list_item(source)
        target_item = self.get_list_item(target)

        source_item.drag_to(target_item)

    def drag_grid_item_to_item(self, source: str, target: str):
        source_item = self.get_grid_item(source)
        target_item = self.get_grid_item(target)

        source_item.drag_to(target_item)

    def check_list_item_visible(self, name: str):
        expect(self.get_list_item(name)).to_be_visible()

    def check_grid_item_visible(self, name: str):
        expect(self.get_grid_item(name)).to_be_visible()