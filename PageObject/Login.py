from selenium.webdriver.common.by import By
from PageObject.base_page import BasePage
class LoginPage(BasePage):
    user_name =(By.XPATH,"//input[@id='user-name']")
    pass_word =(By.XPATH,"//input[@id='password']")
    login_btn =(By.XPATH,"//input[@id='login-button']")


    def enter_username(self,username):
        self.type(self.user_name,username)
    def enter_password(self, password):
        self.type(self.pass_word,password)
    def click_login(self):
        self.click(self.login_btn)


