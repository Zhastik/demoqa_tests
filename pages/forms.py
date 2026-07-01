from playwright.sync_api import Page, expect


class PracticeForm:
    def __init__(self, page: Page):
        self.page = page

        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.email_input = page.get_by_placeholder("name@example.com")
        self.mobile_input = page.get_by_placeholder("Mobile Number")
        self.date_of_birth_input = page.get_by_role("textbox", name="")
        self.current_address_input = page.get_by_placeholder("Current Address")

        self.gender_male = page.get_by_label("Male")
        self.gender_female = page.get_by_label("Female")
        self.gender_other = page.get_by_label("Other")

        self.hobby_sports = page.get_by_label("Sports")
        self.hobby_reading = page.get_by_label("Reading")
        self.hobby_music = page.get_by_label("Music")

        self.submit_button = page.get_by_role("button", name="Submit")

        self.modal_title = page.get_by_text("Thanks for submitting the form")

    def navigate(self):
        self.page.goto("https://demoqa.com/automation-practice-form")

    def fill_student_data(
        self,
        first_name: str,
        last_name: str,
        email: str,
        mobile: str,
        address: str
    ):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.email_input.fill(email)
        self.mobile_input.fill(mobile)
        self.current_address_input.fill(address)

    def select_gender(self, gender: str):
        self.page.get_by_label(gender, exact=True).check()

    def select_hobby(self, hobby: str):
        self.page.get_by_label(hobby, exact=True).check()

    def select_subject(self, subject: str):
        subject_input = self.page.get_by_role("combobox").nth(0)
        subject_input.fill(subject)
        subject_input.press("Enter")

    def select_state_and_city(self, state: str, city: str):
        state_input = self.page.get_by_role("combobox").nth(1)
        state_input.fill(state)
        state_input.press("Enter")

        city_input = self.page.get_by_role("combobox").nth(2)
        city_input.fill(city)
        city_input.press("Enter")

    def submit(self):
        self.submit_button.scroll_into_view_if_needed()
        self.submit_button.click()

    def check_modal_opened(self):
        expect(self.modal_title).to_be_visible()