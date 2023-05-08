import pytest
from test_base import TestBase
from assertpy import assert_that, soft_assertions
from util.constants import Constants


class TestEndToEnd(TestBase):

    @pytest.fixture(scope='class', autouse=True)
    def env_preparation(self):
        global textbox_page
        textbox_page = self.textbox_page
        super().choose_elements()
        textbox_page.click_text_box_button()

    def test_successful_filling_text_box(self):
        textbox_page.entering_text_into_boxes()
        assert textbox_page.find_field_with_entering_values(), 'THERE WASN\'T FIELD WITH THE RESULTS'

    def test_right_text_in_result_field(self):
        with soft_assertions():
            assert_that(f'Name:{textbox_page.getter_dict_data()[Constants.NAME]}').is_equal_to(textbox_page.get_text_name())
            assert_that(f'Email:{textbox_page.getter_dict_data()[Constants.EMAIL]}').is_equal_to(textbox_page.get_text_email())
            assert_that(f'Current Address :{textbox_page.getter_dict_data()[Constants.CURRENT_ADDRESS]}').is_equal_to(
                textbox_page.get_text_current_address())
            assert_that(f'Permananet Address :{textbox_page.getter_dict_data()[Constants.PERMANENT_ADDRESS]}').is_equal_to(
                textbox_page.get_text_permanent_address())
