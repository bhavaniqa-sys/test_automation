from selenium.webdriver.common.by import By
from PageObject.base_page import BasePage


class Checkout(BasePage):

    first_name = (By.ID,"first-name")
    last_name = (By.CSS_SELECTOR,"#last-name")
    zip_code = (By.XPATH,"//input[@name='postalCode']")
    click_cont_btn=(By.ID,"continue")
    click_finsh_btn=(By.CSS_SELECTOR,"#finish")
    confirmation_msg = (By.XPATH,"//h2[text()='Thank you for your order!']")


    def enter_first_name(self,fname):
        self.type(self.first_name,fname)
    def enter_last_name(self,lname):
        self.type(self.last_name,lname)
    def enter_zip_code(self,zip):
        self.type(self.zip_code,zip)
    def continue_button(self):
        self.click(self.click_cont_btn)
    def finish_button(self):
        self.click(self.click_finsh_btn)
    def confirm_msg_text(self):
        return self.get_text(self.confirmation_msg)

