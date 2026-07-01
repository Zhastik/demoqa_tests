from playwright.sync_api import Page, expect


class Droppable:
    def __init__(self, page: Page):
        self.page = page

        self.simple_tab = page.get_by_role("tab", name="Simple")
        self.accept_tab = page.get_by_role("tab", name="Accept")
        self.prevent_tab = page.get_by_role("tab", name="Prevent Propogation")
        self.revert_tab = page.get_by_role("tab", name="Revert Draggable")

        self.simple_panel = page.get_by_role("tabpanel", name="Simple")
        self.accept_panel = page.get_by_role("tabpanel", name="Accept")
        self.prevent_panel = page.get_by_role("tabpanel", name="Prevent Propogation")
        self.revert_panel = page.get_by_role("tabpanel", name="Revert Draggable")

    def navigate(self):
        self.page.goto("https://demoqa.com/droppable")

    def open_simple_tab(self):
        self.simple_tab.click()

    def open_accept_tab(self):
        self.accept_tab.click()

    def open_prevent_tab(self):
        self.prevent_tab.click()

    def open_revert_tab(self):
        self.revert_tab.click()

    def drag_and_drop(self, source, target):
        source_box = source.bounding_box()
        target_box = target.bounding_box()

        source_x = source_box["x"] + source_box["width"] / 2
        source_y = source_box["y"] + source_box["height"] / 2

        target_x = target_box["x"] + target_box["width"] / 2
        target_y = target_box["y"] + target_box["height"] / 2

        self.page.mouse.move(source_x, source_y)
        self.page.mouse.down()
        self.page.mouse.move(target_x, target_y, steps=20)
        self.page.mouse.up()

    def drag_simple_box_to_drop_area(self):
        source = self.simple_panel.get_by_text("Drag Me", exact=True)
        target = self.simple_panel.get_by_text("Drop Here", exact=True)

        self.drag_and_drop(source, target)

    def drag_acceptable_to_drop_area(self):
        source = self.accept_panel.get_by_text("Acceptable", exact=True)
        target = self.accept_panel.get_by_text("Drop here", exact=True)

        self.drag_and_drop(source, target)

    def drag_not_acceptable_to_drop_area(self):
        source = self.accept_panel.get_by_text("Not Acceptable", exact=True)
        target = self.accept_panel.get_by_text("Drop here", exact=True)

        self.drag_and_drop(source, target)

    def drag_to_not_greedy_inner_box(self):
        source = self.prevent_panel.get_by_text("Drag Me", exact=True)
        target = self.prevent_panel.get_by_text("Inner droppable (not greedy)", exact=True)

        self.drag_and_drop(source, target)

    def drag_to_greedy_inner_box(self):
        source = self.prevent_panel.get_by_text("Drag Me", exact=True)
        target = self.prevent_panel.get_by_text("Inner droppable (greedy)", exact=True)

        self.drag_and_drop(source, target)

    def drag_will_revert_to_drop_area(self):
        source = self.revert_panel.get_by_text("Will Revert", exact=True)
        target = self.revert_panel.get_by_text("Drop here", exact=True)

        self.drag_and_drop(source, target)

    def drag_not_revert_to_drop_area(self):
        source = self.revert_panel.get_by_text("Not Revert", exact=True)
        target = self.revert_panel.get_by_text("Drop here", exact=True)

        self.drag_and_drop(source, target)

    def check_simple_dropped(self):
        expect(self.simple_panel.get_by_text("Dropped!", exact=True)).to_be_visible()

    def check_accept_dropped(self):
        expect(self.accept_panel.get_by_text("Dropped!", exact=True)).to_be_visible()

    def check_accept_not_dropped(self):
        expect(self.accept_panel.get_by_text("Drop here", exact=True)).to_be_visible()

    def check_prevent_dropped(self):
        expect(self.prevent_panel.get_by_text("Dropped!", exact=True)).to_be_visible()

    def check_revert_dropped(self):
        expect(self.revert_panel.get_by_text("Dropped!", exact=True)).to_be_visible()