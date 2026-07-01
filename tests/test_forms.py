import pytest
from pages.forms import PracticeForm


@pytest.mark.parametrize(
    "first_name, last_name, email, gender, mobile, subject, hobby, address, state, city",
    [
        (
            "Jes",
            "Test",
            "jes@mail.ru",
            "Male",
            "1234567890",
            "Maths",
            "Sports",
            "Lenina aven",
            "NCR",
            "Delhi",
        )
    ]
)
def test_practice_form(
    page,
    first_name,
    last_name,
    email,
    gender,
    mobile,
    subject,
    hobby,
    address,
    state,
    city
):
    practice_form_page = PracticeForm(page)

    practice_form_page.navigate()

    practice_form_page.fill_student_data(
        first_name=first_name,
        last_name=last_name,
        email=email,
        mobile=mobile,
        address=address,
    )

    practice_form_page.select_gender(gender)
    practice_form_page.select_subject(subject)
    practice_form_page.select_hobby(hobby)
    practice_form_page.select_state_and_city(state, city)

    practice_form_page.submit()
    practice_form_page.check_modal_opened()