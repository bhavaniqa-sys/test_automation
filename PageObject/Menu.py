from selenium.webdriver.common.by import By
from PageObject.base_page import BasePage

class MenuPage(BasePage):
    open_menu_for_all_items = (By.XPATH, "//button[text()='Open Menu']")
    logout_btn = (By.XPATH, "//a[contains(@id,'logout')]")

    def open_menu(self):
        self.click(self.open_menu_for_all_items)
    def click_logout(self):
        self.click(self.logout_btn)
