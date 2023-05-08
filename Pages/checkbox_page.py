from Pages.base_page import BasePage
from util.locators import Checkbox


class CheckboxPageObject(BasePage):
    def click_checkbox_button(self):
        super().element_click(Checkbox.BUTTON_CHECKBOX)

    def click_button_toggle(self):
        super().element_click(Checkbox.BUTTON_TOGGLE)
        super().element_click(Checkbox.BUTTON_TOGGLE_2)
        super().element_click(Checkbox.CHECKBOX_NOTES)

    def checking_element_selected(self):
        return super().is_element_selected(Checkbox.CHECKBOX_NOTES_FOR_CHECKING)

    def finding_result_field(self):
        return super().find_need_element(Checkbox.FIELD_WITH_INFO_RESULT)

    def get_text_from_result(self):
        return super().get_elements_text(Checkbox.TEXT_RESULTS)

    def get_text_from_choosing_checkbox(self):
        return super().get_elements_text(Checkbox.TEXT_CHOOSING_CHECKBOX).lower()
