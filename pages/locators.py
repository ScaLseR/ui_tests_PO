from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR,
                  ".desk-notif-card__login-new-item-title.desk-notif-card__login-new-item-title")
    DISK_LINK = (By.CSS_SELECTOR, ".btn-group .btn-default")


class LoginPageLocators:
    EMAIL = (By.CSS_SELECTOR, ".Textinput-Control")
    PASS = (By.CSS_SELECTOR, ".Textinput-Control")
    BTN_LOG = (By.ID, "passp:sign-in")
    BTN_LOG_2 = (By.ID, "passp:sign-in")