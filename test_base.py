import pytest

from Pages.alerts_page import AlertsPageObject
from Pages.checkbox_page import CheckboxPageObject
from Pages.textbox_page import TextBoxPageObject
from Pages.main_page import MainPageObject
from util.constants import Constants


class TestBase:
    @pytest.fixture(scope='class', autouse=True)
    def before_all(self, get_browser):
        global main_page
        main_page = MainPageObject(get_browser, Constants.link_site)
        self.textbox_page = TextBoxPageObject(get_browser, Constants.link_site)
        self.checkbox_page = CheckboxPageObject(get_browser, Constants.link_site)
        self.alerts_page = AlertsPageObject(get_browser, Constants.link_site)
        main_page.open()

    @staticmethod
    def choose_elements():
        main_page.click_elements_button()

    @staticmethod
    def choose_alerts():
        main_page.click_alerts_button()
