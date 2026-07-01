from playwright.sync_api import expect


class Links:
    def __init__(self, page):
        self.page = page

        self.created_link = page.locator("#created")
        self.no_content_link = page.locator("#no-content")
        self.moved_link = page.locator("#moved")
        self.bad_request_link = page.locator("#bad-request")
        self.unauthorized_link = page.locator("#unauthorized")
        self.forbidden_link = page.locator("#forbidden")
        self.not_found_link = page.locator("#invalid-url")

        self.link_response = page.locator("#linkResponse")

    def navigate(self):
        self.page.goto("https://demoqa.com/links")

    def check_response(self, status_code, status_text):
        expect(self.link_response).to_have_text(
            f"Link has responded with staus {status_code} and status text {status_text}"
        )