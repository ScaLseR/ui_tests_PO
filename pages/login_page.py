from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    """class for work with login page"""

    def authorized_user(self, login, password):
        inp_login = self.browser.find_element(*LoginPageLocators.EMAIL)
        inp_login.send_keys(login)
        btn_log_1 = self.browser.find_element(*LoginPageLocators.BTN_LOG)
        btn_log_1.click()
        time.sleep(2)
        inp_pass = self.browser.find_element(*LoginPageLocators.PASS)
        inp_pass.send_keys(password)
        btn_log_2 = self.browser.find_element(*LoginPageLocators.BTN_LOG)
        btn_log_2.click()
        time.sleep(60)
