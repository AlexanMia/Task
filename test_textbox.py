import pytest
from test_base import TestBase
from assertpy import assert_that, soft_assertions
from util.constants import Constants


class TestEndToEndTextbox(TestBase):
    @pytest.fixture(scope='class', autouse=True)
    def env_preparation(self):
        global textbox_page
        textbox_page = self.textbox_page
        super().choose_elements()
        textbox_page.click_text_box_button()

    def test_successful_filling_text_box(self):
        textbox_page.entering_text_into_boxes()
        with soft_assertions():
            assert_that(textbox_page.find_field_with_entering_values()) \
                .described_as('There is a field with the results') \
                .is_true()

    def test_right_text_in_result_field(self):
        with soft_assertions():
            assert_that(textbox_page.get_text_name()) \
                .described_as(
                f'Check name in the result field is equal to {textbox_page.getter_dict_data()[Constants.NAME]}') \
                .is_equal_to(f'Name:{textbox_page.getter_dict_data()[Constants.NAME]}')

            assert_that(textbox_page.get_text_email()) \
                .described_as(
                f'Check email in the result field is equal to {textbox_page.getter_dict_data()[Constants.EMAIL]}') \
                .is_equal_to(f'Email:{textbox_page.getter_dict_data()[Constants.EMAIL]}')

            assert_that(textbox_page.get_text_current_address()) \
                .described_as(
                f'Check current address in the result field is equal to {textbox_page.getter_dict_data()[Constants.EMAIL]}') \
                .is_equal_to(f'Current Address :{textbox_page.getter_dict_data()[Constants.CURRENT_ADDRESS]}')

            assert_that(textbox_page.get_text_permanent_address()) \
                .described_as(
                f'Check permanent address in the result field is equal to {textbox_page.getter_dict_data()[Constants.EMAIL]}') \
                .is_equal_to(f'Permananet Address :{textbox_page.getter_dict_data()[Constants.PERMANENT_ADDRESS]}')
