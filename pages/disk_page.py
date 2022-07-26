from .base_page import BasePage
from .locators import DiskPageLocators
import time


class DiskPage(BasePage):
    """class for work with yandex disk page"""

    def copy_file_to_folder(self, file_name, folder_name):
        BasePage.go_to_new_window(self)
        self.click_file(file_name)
        self.click_btn_to_copy()
        self.click_to_folder_in_copy_menu(folder_name)
        self.click_btn_copy_in_copy_menu()
        time.sleep(300)

    def click_btn_to_copy(self):
        if BasePage.is_element_present(*DiskPageLocators.BTN_TO_COPY):
            btn_to_copy = self.browser.find_element(*DiskPageLocators.BTN_TO_COPY)
            btn_to_copy.click()
        else:
            self.click_btn_menu_all()

    def click_file(self, file_name):
        file_to_click = self.browser.find_element(DiskPageLocators.FILE, f'[aria-label^="{file_name}"]')
        file_to_click.click()

    def click_to_folder_in_copy_menu(self, folder_name):
        folder_to_click = self.browser.find_element(DiskPageLocators.FOLDER, f'[title="{folder_name}"]')
        folder_to_click.click()

    def click_btn_copy_in_copy_menu(self):
        btn_copy = self.browser.find_element(DiskPageLocators.FOLDER)
        btn_copy.click()

    def click_btn_menu_all(self):
        btn_all = self.browser.find_element(*DiskPageLocators.BTN_ALL)
        btn_all.click()

    def click_btn_copy_menu_all(self):
        btn_copy_all = self.browser.find_element(*DiskPageLocators.BTN_COPY_MENU_ALL)
        btn_copy_all.click()

