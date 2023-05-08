from Pages.base_page import BasePage
from util.locators import Alerts


class AlertsPageObject(BasePage):

    def click_alerts_menu_button(self):
        super().element_click(Alerts.BUTTON_MENU_ALERTS)

    def switch_to_alert(self):
        return self.browser.switch_to_alert()

    def get_text_from_alert(self):
        return self.browser.switch_to_alert().text

    def post_text_to_alert(self, text):
        return self.browser.switch_to_alert().send_keys(text)

    def accept_alert(self):
        self.switch_to_alert().accept()

    def click_button_open_alert_timer(self):
        super().element_click(Alerts.BUTTON_OPEN_ALERT_TIMER)

    def click_button_open_alert_confirm(self):
        super().element_click(Alerts.BUTTON_OPEN_ALERT_CONFIRM)

    def click_button_open_alert_prompt(self):
        super().element_click(Alerts.BUTTON_OPEN_ALERT_PROMPT)

    def find_results_confirm_field(self):
        return super().find_need_element(Alerts.CONFIRM_RESULT)

    def text_from_result_confirm_field(self):
        return super().get_elements_text(Alerts.CONFIRM_RESULT)

    def find_results_prompt_field(self):
        return super().find_need_element(Alerts.PROMPT_RESULT)

    def text_from_result_prompt_field(self):
        return super().get_elements_text(Alerts.PROMPT_RESULT)
