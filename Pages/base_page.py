import random
import string

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def find_need_element(self, locator):
        return self.browser.find_element(*locator)

    def element_click(self, locator):
        return self.find_need_element(locator).click()

    def enter_value_into_box(self, locator, meaning):
        return self.find_need_element(locator).send_keys(meaning)

    def get_elements_text(self, locator):
        return self.find_need_element(locator).text

    def is_element_selected(self, locator):
        return self.find_need_element(locator).is_selected()

    def random_alphanumeric_string(self, count):
        return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(count)])

    def random_email(self, count1, count2, count3):
        return f'{self.random_alphanumeric_string(count1)}@{self.random_alphanumeric_string(count2)}.{self.random_alphanumeric_string(count3)}'

    def waiting_alert(self):
        WebDriverWait(self.browser, timeout=7).until(expected_conditions.alert_is_present())
