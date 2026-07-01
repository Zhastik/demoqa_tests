from pages.elements.text_box import TextBox
import pytest
from pages.elements.radio_button import RadioButton
from pages.elements.links import Links
from pages.elements.buttons import Buttons
from pages.elements.upload_download import UploadDownload


@pytest.mark.parametrize("name, email, current, permanent", [(
    "jes", "jes@mail.ru", "lenim aven", "sadsadsa"
)])
def test_text_box(page, name, email, current, permanent):
    text_box_page = TextBox(page)
    text_box_page.navigate()
    text_box_page.login_poz(name, email, current, permanent)
    result = text_box_page.get_result_massege()
    assert result[0] == f"Name:{name}"
    assert result[1] == f"Email:{email}"
    assert result[2] == f"Current Address :{current}"
    assert result[3] == f"Permananet Address :{permanent}"

def test_radio_button_yes(page):
    radio_button_page = RadioButton(page)
    radio_button_page.navigate()

    radio_button_page.click_yes()

    radio_button_page.check_yes_selected()


def test_radio_button_impressive(page):
    radio_button_page = RadioButton(page)
    radio_button_page.navigate()

    radio_button_page.click_impressive()

    radio_button_page.check_impressive_selected()


def test_radio_button_no_is_disabled(page):
    radio_button_page = RadioButton(page)
    radio_button_page.navigate()

    radio_button_page.check_no_disabled()

def test_double_click_button(page):
    buttons_page = Buttons(page)
    buttons_page.navigate()

    buttons_page.double_click()

    buttons_page.check_double_click_message()


def test_right_click_button(page):
    buttons_page = Buttons(page)
    buttons_page.navigate()

    buttons_page.right_click()

    buttons_page.check_right_click_message()


def test_click_me_button(page):
    buttons_page = Buttons(page)
    buttons_page.navigate()

    buttons_page.click_me()

    buttons_page.check_dynamic_click_message()

@pytest.mark.parametrize("link_name, status_code, status_text", [
    ("created_link", 201, "Created"),
    ("no_content_link", 204, "No Content"),
    ("moved_link", 301, "Moved Permanently"),
    ("bad_request_link", 400, "Bad Request"),
    ("unauthorized_link", 401, "Unauthorized"),
    ("forbidden_link", 403, "Forbidden"),
    ("not_found_link", 404, "Not Found"),
])
def test_api_links(page, link_name, status_code, status_text):
    links_page = Links(page)
    links_page.navigate()

    getattr(links_page, link_name).click()

    links_page.check_response(status_code, status_text)

def test_download_file(page, tmp_path):
    upload_download_page = UploadDownload(page)
    upload_download_page.navigate()

    download = upload_download_page.download_file()

    assert download.suggested_filename == "sampleFile.jpeg"

    save_path = tmp_path / download.suggested_filename
    download.save_as(save_path)

    assert save_path.exists()


def test_upload_file(page, tmp_path):
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("Hello Playwright", encoding="utf-8")

    upload_download_page = UploadDownload(page)
    upload_download_page.navigate()

    upload_download_page.upload(file_path)

    upload_download_page.check_uploaded_file("test_file.txt")