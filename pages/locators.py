from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, ".desk-notif-card__login-new-item-title.desk-notif-card__login-new-item-title")
    DISK_LINK = (By.CSS_SELECTOR, ".btn-group .btn-default")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL = (By.ID, "id_registration-email")
    PASS = (By.ID, "id_registration-password1")
    CONF_PASS = (By.ID, "id_registration-password2")
    BTN_LOG = (By.NAME, "registration_submit")
    LOGOUT = (By.ID, "logout_link")