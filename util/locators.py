from selenium.webdriver.common.by import By


class MainPage:
    BUTTON_MENU_ELEMENTS = (By.CSS_SELECTOR, 'div.card.mt-4.top-card')
    BUTTON_MENU_ALERTS_FRAME = (By.CSS_SELECTOR, 'div > div:nth-child(3) > div')


class TextBox:
    BUTTON_TEXT_BOX = (By.ID, 'item-0')
    FULL_NAME_TEXT_BOX = (By.ID, 'userName')
    EMAIL_TEXT_BOX = (By.ID, 'userEmail')
    CURRENT_ADDRESS_TEXT_BOX = (By.ID, 'currentAddress')
    PERMANENT_ADDRESS_TEXT_BOX = (By.ID, 'permanentAddress')

    BUTTON_SUBMIT = (By.ID, 'submit')

    FIELD_WITH_RESULTS = (By.ID, 'output')
    RESULT_NAME = (By.ID, 'name')
    RESULT_EMAIL = (By.ID, 'email')
    RESULT_CURRENT_ADDRESS = (By.CSS_SELECTOR, 'div.border > #currentAddress')
    RESULT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'div.border > #permanentAddress')


class Checkbox:
    BUTTON_CHECKBOX = (By.ID, 'item-1')

    BUTTON_TOGGLE = (By.CLASS_NAME, 'rct-collapse-btn')
    BUTTON_TOGGLE_INNER = (By.XPATH, '//label[@for="tree-node-desktop"]/../button')

    CHECKBOX_COMMANDS = (By.CLASS_NAME, 'rct-icon-check')

    CHECKBOX_NOTES = (By.CSS_SELECTOR, 'label[for="tree-node-notes"] > span.rct-checkbox')
    CHECKBOX_NOTES_FOR_CHECKING = (By.CSS_SELECTOR, 'label[for="tree-node-notes"] > input#tree-node-notes')
    FIELD_WITH_INFO_RESULT = (By.CSS_SELECTOR, 'div#result')
    TEXT_RESULTS = (By.CSS_SELECTOR, 'div#result > span.text-success')
    TEXT_CHOOSING_CHECKBOX = (By.CSS_SELECTOR, 'label[for="tree-node-notes"] > span.rct-title')


class Alerts:
    BUTTON_MENU_ALERTS = (By.XPATH, '//span[text()="Alerts"]')

    BUTTON_OPEN_ALERT_TIMER = (By.ID, 'timerAlertButton')
    BUTTON_OPEN_ALERT_CONFIRM = (By.ID, 'confirmButton')
    BUTTON_OPEN_ALERT_PROMPT = (By.ID, 'promtButton')

    CONFIRM_RESULT = (By.CSS_SELECTOR, 'span#confirmResult')
    PROMPT_RESULT = (By.ID, 'promptResult')
