from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR,
                  '.desk-notif-card__login-new-item-title.desk-notif-card__login-new-item-title')
    DISK_LINK = (By.CSS_SELECTOR, '.desk-notif-card__domik-item .home-link.home-link_black_yes')


class LoginPageLocators:
    BTN_EMAIL = (By.CSS_SELECTOR, '.Button2.Button2_size_l.Button2_view_default')
    EMAIL = (By.ID, 'passp-field-login')
    PASS = (By.CSS_SELECTOR, '.Textinput-Control')
    BTN_LOG = (By.ID, 'passp:sign-in')
    BTN_LOG_2 = (By.ID, 'passp:sign-in')