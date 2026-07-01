from playwright.sync_api import expect


class UploadDownload:
    def __init__(self, page):
        self.page = page

        self.download_button = page.locator("#downloadButton")
        self.upload_file = page.locator("#uploadFile")
        self.uploaded_file_path = page.locator("#uploadedFilePath")

    def navigate(self):
        self.page.goto("https://demoqa.com/upload-download")

    def download_file(self):
        with self.page.expect_download() as download_info:
            self.download_button.click()

        return download_info.value

    def upload(self, file_path):
        self.upload_file.set_input_files(str(file_path))

    def check_uploaded_file(self, file_name):
        expect(self.uploaded_file_path).to_contain_text(file_name)