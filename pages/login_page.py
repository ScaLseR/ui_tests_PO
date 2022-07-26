from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """class for work with login page"""

    def authorized_user(self, login, password):
        inp_login = self.browser.find_element(*LoginPageLocators.EMAIL)
        inp_login.send_keys(login)
        inp_pass = self.browser.find_element(*LoginPageLocators.PASS)
        inp_pass.send_keys(password)
        inp_confirm_pass = self.browser.find_element(*LoginPageLocators.CONF_PASS)
        inp_confirm_pass.send_keys(password)
        btn_reg = self.browser.find_element(*LoginPageLocators.BTN_REG)
        btn_reg.click()

    def user_login_to_account(self):
        assert self.is_element_present(*LoginPageLocators.LOGOUT), "Пользователь не зашел в аккаунт, регистрация не " \
                                                                   "проведена! "
