from .base_page import BasePage
from .locators import LoginPageLocators
from time import sleep


class LoginPage(BasePage):
    """class for work with login page"""

    def authorized_user(self, login, password):
        """user authorization """
        self.select_authorization_by_email()
        self.enter_login(login)
        self.click_btn_log()
        self.enter_password(password)
        self.click_btn_log()

    def select_authorization_by_email(self):
        """select authorization by email"""
        btn_email = self.browser.find_element(*LoginPageLocators.BTN_EMAIL)
        btn_email.click()

    def enter_login(self, login):
        """entering login into field email"""
        inp_login = self.browser.find_element(*LoginPageLocators.EMAIL)
        inp_login.send_keys(login)

    def click_btn_log(self):
        """clicking button Enter"""
        btn_log = self.browser.find_element(*LoginPageLocators.BTN_LOG)
        btn_log.click()

    def enter_password(self, password):
        """entering password into field password"""

        inp_pass = self.browser.find_element(*LoginPageLocators.PASS)
        inp_pass.send_keys(password)
