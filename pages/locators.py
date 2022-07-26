from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    DISK_LINK = (By.CSS_SELECTOR, ".btn-group .btn-default")

