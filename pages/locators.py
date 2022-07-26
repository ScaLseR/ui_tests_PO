from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR,
                  '.desk-notif-card__login-new-item-title.desk-notif-card__login-new-item-title')
    DISK_LINK = (By.CSS_SELECTOR, '[data-statlog="notifications.mail.login.disk"]')


class LoginPageLocators:
    BTN_EMAIL = (By.CSS_SELECTOR, '[data-type="login"]')
    EMAIL = (By.ID, 'passp-field-login')
    PASS = (By.ID, 'passp-field-passwd')
    BTN_LOG = (By.ID, 'passp:sign-in')


class DiskPageLocators:
    FILE = (By.CSS_SELECTOR)
    FOLDER = (By.CSS_SELECTOR)
    BTN_TO_COPY_TOP_MENU = (By.CSS_SELECTOR, '[aria-label="Копировать"]')
    BTN_COPY_IN_COPY_DIALOG = (By.CSS_SELECTOR,
                '.Button2.Button2_view_action.Button2_size_m.confirmation-dialog_'
                '_button.confirmation-dialog__button_submit ')
    BTN_ALL = (By.CSS_SELECTOR, '[aria-label="Ещё"]')
    BTN_COPY_MENU_ALL = (By.CSS_SELECTOR, '.Menu-Text')