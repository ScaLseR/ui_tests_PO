"""Test Cases Module"""
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.disk_page import DiskPage


_FILE_NAME = 'Файл для копирования'
_FOLDER_NAME = 'Задание_2'
_URL = 'http://yandex.ru'
_LOGIN = 'simbirsofttzskorik'
_PASSWORD = '123qazqwe!@#'


def test_copy_file_to_folder(browser):
    """test case"""
    page = MainPage(browser, _URL)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.authorized_user(_LOGIN, _PASSWORD)
    login_page.go_to_disk_page()
    disk_page = DiskPage(browser, browser.current_url)
    disk_page.copy_file_to_folder(_FILE_NAME, _FOLDER_NAME)
    disk_page.open_folder_in_disk(_FOLDER_NAME)
    disk_page.delete_files_in_folder(_FILE_NAME)
    assert disk_page.count_files_in_folder() == 1
    assert disk_page.get_file_name() == _FILE_NAME
    disk_page.logout()
