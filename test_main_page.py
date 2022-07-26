from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest


def test_enable_login_page(browser):
    page = MainPage(browser, "http://yandex.ru")
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.authorized_user('simbirsofttzskorik', '123qazqwe!@#')
