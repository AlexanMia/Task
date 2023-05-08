import time

import pytest
from test_base import TestBase


class TestEndToEnd(TestBase):
    @pytest.fixture(scope='class', autouse=True)
    def env_preparation(self):
        global checkbox_page
        checkbox_page = self.checkbox_page
        super().choose_elements()
        checkbox_page.click_checkbox_button()

    def test_successful_choose_checkbox(self):
        checkbox_page.click_button_toggle()

        assert checkbox_page.checking_element_selected(), 'CheckBox is not selected'
        assert checkbox_page.finding_result_field(), 'There is not a result\'s field'
        assert checkbox_page.get_text_from_result() == checkbox_page.get_text_from_choosing_checkbox(), \
            f'{checkbox_page.get_text_from_result()}!={checkbox_page.get_text_from_choosing_checkbox()}'
