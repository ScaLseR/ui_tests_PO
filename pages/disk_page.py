from .base_page import BasePage
from .locators import DiskPageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains


class DiskPage(BasePage):
    """class for work with yandex disk page"""

    def open_folder_in_disk(self, folder_name):
        """opening folder with name = folder_name on disk"""
        self.double_click_folder_on_disk(folder_name)

    def copy_file_to_folder(self, file_name, folder_name):
        """copy file name = file_name to folder name = folder_name """
        BasePage.go_to_new_window(self)
        self.click_file(file_name)
        self.click_btn_to_copy()
        self.click_to_folder_in_copy_menu(folder_name)
        self.click_btn_copy_in_copy_menu()

    def is_element_present(self, how, what):
        """find element on page"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def click_btn_to_copy(self):
        """clicking button Copy"""
        btn_to_copy = self.browser.find_element(*DiskPageLocators.BTN_TO_COPY_TOP_MENU)
        if btn_to_copy.is_enabled() and btn_to_copy.is_displayed():
            btn_to_copy.click()
        else:
            self.click_btn_menu_all()
            self.click_btn_copy_menu_all()

    def click_file(self, file_name):
        """one click left mouse button on file name = file_name """
        while not self.is_element_present(DiskPageLocators.FILE, f'[aria-label^="{file_name}"]'):
            self.browser.implicitly_wait(1)
        file_to_click = self.browser.find_element(DiskPageLocators.FILE, f'[aria-label^="{file_name}"]')
        file_to_click.click()

    def click_to_folder_in_copy_menu(self, folder_name):
        """select folder name = folder_name in copy menu"""
        folder_to_click = self.browser.find_element(DiskPageLocators.FOLDER, f'[title="{folder_name}"]')
        folder_to_click.click()

    def double_click_folder_on_disk(self, folder_name):
        """opening folder name = folder_name on disk (double click left mouse button)"""
        folder_to_click = self.browser.find_element(DiskPageLocators.FOLDER, f'[aria-label="{folder_name}"]')
        action = ActionChains(self.browser)
        action.double_click(folder_to_click).perform()

    def click_btn_copy_in_copy_menu(self):
        """clicking button Copy in copy menu"""
        btn_copy = self.browser.find_element(*DiskPageLocators.BTN_COPY_IN_COPY_DIALOG)
        btn_copy.click()

    def click_btn_menu_all(self):
        """open menu all (...)"""
        btn_all = self.browser.find_element(*DiskPageLocators.BTN_ALL)
        btn_all.click()

    def click_btn_copy_menu_all(self):
        """clicking button Copy in menu all (...)"""
        btn_copy_all = self.browser.find_element(*DiskPageLocators.BTN_COPY_MENU_ALL)
        btn_copy_all.click()

    def delete_files_in_folder(self, file_name):
        """deleting all files in folder with name != file_name"""
        while not self.is_element_present(DiskPageLocators.FILE, f'[aria-label^="{file_name}"]'):
            self.browser.implicitly_wait(1)
        count = self.count_files_in_folder()
        if count > 1:
            names = self.get_files_names()
            for name in names:
                if name != file_name:
                    self.delete_one_file(name)

    def count_files_in_folder(self):
        """count all files in folder"""
        files = self.browser.find_elements(*DiskPageLocators.FILES_ALL)
        return len(files)

    def get_files_names(self):
        """get all files names in folder"""
        files = self.browser.find_elements(*DiskPageLocators.FILES_NAMES_ALL)
        texts = [name.get_attribute("aria-label").split('.')[0] for name in files]
        return texts

    def delete_one_file(self, file_name):
        """deleting one file with name = file name"""
        self.click_file(file_name)
        btn_delete = self.browser.find_element(*DiskPageLocators.BTN_DELETE)
        btn_delete.click()
        self.browser.implicitly_wait(1)

    def get_file_name(self):
        """get last one file name in folder"""
        name = self.browser.find_element(*DiskPageLocators.FILES_NAMES_ALL)
        text = name.get_attribute("aria-label").split('.')[0]
        return text
