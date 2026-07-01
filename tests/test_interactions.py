from pages.interactions.sortable import Sortable
from pages.interactions.selectable import Selectable


def test_sortable_list(page):
    sortable_page = Sortable(page)

    sortable_page.navigate()
    sortable_page.open_list_tab()

    sortable_page.drag_list_item_to_item("One", "Two")

    sortable_page.check_list_item_visible("One")
    sortable_page.check_list_item_visible("Two")

def test_sortable_grid(page):
    sortable_page = Sortable(page)

    sortable_page.navigate()
    sortable_page.open_grid_tab()

    sortable_page.drag_grid_item_to_item("One", "Two")

    sortable_page.check_grid_item_visible("One")
    sortable_page.check_grid_item_visible("Two")

def test_selectable_list(page):
    selectable_page = Selectable(page)

    selectable_page.navigate()
    selectable_page.open_list_tab()

    selectable_page.select_list_item("Cras justo odio")

    selectable_page.check_list_item_selected("Cras justo odio")

def test_selectable_grid(page):
    selectable_page = Selectable(page)

    selectable_page.navigate()
    selectable_page.open_grid_tab()

    selectable_page.select_grid_item("Five")

    selectable_page.check_grid_item_selected("Five")