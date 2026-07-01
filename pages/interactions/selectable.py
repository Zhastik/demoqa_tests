from playwright.sync_api import Page


class Selectable:
    def __init__(self, page: Page):
        self.page = page

        self.list_tab = page.get_by_role("tab", name="List")
        self.grid_tab = page.get_by_role("tab", name="Grid")

        self.list_panel = page.get_by_role("tabpanel", name="List")
        self.grid_panel = page.get_by_role("tabpanel", name="Grid")

    def navigate(self):
        self.page.goto("https://demoqa.com/selectable")

    def open_list_tab(self):
        self.list_tab.click()

    def open_grid_tab(self):
        self.grid_tab.click()

    def get_list_item(self, text: str):
        return self.list_panel.get_by_text(text, exact=True)

    def get_grid_item(self, text: str):
        return self.grid_panel.get_by_text(text, exact=True)

    def select_list_item(self, text: str):
        self.get_list_item(text).click()

    def select_grid_item(self, text: str):
        self.get_grid_item(text).click()

    def is_item_selected(self, item):
        class_name = item.get_attribute("class")
        return "active" in class_name.split()

    def check_list_item_selected(self, text: str):
        item = self.get_list_item(text)
        assert self.is_item_selected(item)

    def check_grid_item_selected(self, text: str):
        item = self.get_grid_item(text)
        assert self.is_item_selected(item)

    def check_list_item_not_selected(self, text: str):
        item = self.get_list_item(text)
        assert not self.is_item_selected(item)

    def check_grid_item_not_selected(self, text: str):
        item = self.get_grid_item(text)
        assert not self.is_item_selected(item)