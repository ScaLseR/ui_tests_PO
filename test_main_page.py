from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.disk_page import DiskPage


def test_copy_file_to_folder(browser):
    page = MainPage(browser, 'http://yandex.ru')
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.authorized_user('simbirsofttzskorik', '123qazqwe!@#')
    login_page.go_to_disk_page()
    disk_page = DiskPage(browser, browser.current_url)
    disk_page.copy_file_to_folder('Файл для копирования', 'Новая папка')
