import pytest
from assertpy import soft_assertions, assert_that

from test_base import TestBase


class TestEndToEndCheckbox(TestBase):
    @pytest.fixture(scope='class', autouse=True)
    def env_preparation(self):
        global checkbox_page
        checkbox_page = self.checkbox_page
        super().choose_elements()
        checkbox_page.click_checkbox_button()

    def test_successful_choose_checkbox(self):
        checkbox_page.click_button_toggle()

        with soft_assertions():
            assert_that(checkbox_page.checking_element_selected()) \
                .described_as('CheckBox is selected') \
                .is_true()

            assert_that(checkbox_page.finding_result_field()) \
                .described_as('There is a result\'s field') \
                .is_true()

            assert_that(checkbox_page.get_text_from_result()) \
                .described_as('There is a result\'s field') \
                .is_equal_to(checkbox_page.get_text_from_choosing_checkbox())
