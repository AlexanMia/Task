from Pages.base_page import BasePage
from util.constants import Constants
from util.locators import TextBox


class TextBoxPageObject(BasePage):
    def click_text_box_button(self):
        super().element_click(TextBox.BUTTON_TEXT_BOX)

    def entering_text_into_boxes(self):
        self.dict_data = {
            Constants.NAME: f'{super().random_alphanumeric_string()} {super().random_alphanumeric_string()}',
            Constants.EMAIL: super().random_email(),
            Constants.CURRENT_ADDRESS: super().random_alphanumeric_string(),
            Constants.PERMANENT_ADDRESS: super().random_alphanumeric_string()
        }
        super().enter_value_into_box(TextBox.FULL_NAME_TEXT_BOX, self.dict_data[Constants.NAME])
        super().enter_value_into_box(TextBox.EMAIL_TEXT_BOX, self.dict_data[Constants.EMAIL])
        super().enter_value_into_box(TextBox.CURRENT_ADDRESS_TEXT_BOX, self.dict_data[Constants.CURRENT_ADDRESS])
        super().enter_value_into_box(TextBox.PERMANENT_ADDRESS_TEXT_BOX, self.dict_data[Constants.PERMANENT_ADDRESS])
        super().element_click(TextBox.BUTTON_SUBMIT)

    def getter_dict_data(self):
        return self.dict_data

    def find_field_with_entering_values(self):
        return super().find_need_element(TextBox.FIELD_WITH_RESULTS)

    def get_text_name(self):
        return super().get_elements_text(TextBox.RESULT_NAME)

    def get_text_email(self):
        return super().get_elements_text(TextBox.RESULT_EMAIL)

    def get_text_current_address(self):
        return super().get_elements_text(TextBox.RESULT_CURRENT_ADDRESS)

    def get_text_permanent_address(self):
        return super().get_elements_text(TextBox.RESULT_PERMANENT_ADDRESS)
