import pytest
from assertpy import assert_that
from test_base import TestBase
from util.constants import Constants


class TestAlerts(TestBase):
    @pytest.fixture(scope='class', autouse=True)
    def env_preparation(self):
        global alerts_page
        alerts_page = self.alerts_page
        super().choose_alerts()
        alerts_page.click_alerts_menu_button()

    def test_open_alert_timer(self):
        alerts_page.click_button_open_alert_timer()
        alerts_page.waiting_alert()
        alerts_page.switch_to_alert()

        assert_that(alerts_page.get_text_from_alert()) \
            .described_as(f'Check alert_timer text is equal to {Constants.INFO_FROM_ALERT_TIMER}') \
            .is_equal_to(Constants.INFO_FROM_ALERT_TIMER)

        alerts_page.accept_alert()

    def test_open_alert_confirm(self):
        alerts_page.click_button_open_alert_confirm()
        alerts_page.switch_to_alert()

        assert_that(alerts_page.get_text_from_alert()) \
            .described_as(f'Check alert_confirm text is equal to {Constants.INFO_FROM_CONFIRM_ALERT}') \
            .is_equal_to(Constants.INFO_FROM_CONFIRM_ALERT)

        alerts_page.accept_alert()

        assert_that(alerts_page.find_results_confirm_field()) \
            .described_as('There is the field with results') \
            .is_true()

        assert_that(alerts_page.text_from_result_confirm_field()) \
            .described_as(f'Check result of alert_confirm text is equal to {Constants.INFO_FROM_ALERT_ACCEPT}') \
            .is_equal_to(Constants.INFO_FROM_ALERT_ACCEPT)

    def test_open_alert_prompt(self):
        alerts_page.click_button_open_alert_prompt()
        alerts_page.switch_to_alert()

        assert_that(alerts_page.get_text_from_alert()) \
            .described_as(f'Check alert_prompt text is equal to {Constants.INFO_FROM_PROMPT_ALERT}') \
            .is_equal_to(Constants.INFO_FROM_PROMPT_ALERT)

        alerts_page.post_text_to_alert(Constants.NAME_FOR_ALERT)
        alerts_page.accept_alert()

        assert_that(alerts_page.find_results_prompt_field()) \
            .described_as('There is the field with results') \
            .is_true()

        assert_that(alerts_page.text_from_result_prompt_field()) \
            .described_as(f'Check result of alert_confirm text is equal to {Constants.INFO_FROM_PROMPT_ALERT_ACCEPT}') \
            .is_equal_to(Constants.INFO_FROM_PROMPT_ALERT_ACCEPT)
