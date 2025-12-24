from selenium.webdriver.common.by import By
from PageObject.base_page import BasePage

class AddToCart(BasePage):
    product = (By.XPATH,"//div[text()='Sauce Labs Onesie']")
    click_cart = (By.XPATH,"//button[@id='add-to-cart']")
    cart_icon = (By.XPATH,"//a[@class='shopping_cart_link']")
    item_name = (By.XPATH,"//div[@class='inventory_item_name']")

    def click_product(self):
        self.click(self.product)
    def cart_button(self):
        self.click(self.click_cart)
    def click_cart_icon(self):
        self.click(self.cart_icon)
    def selected_product(self):
        return self.get_text(self.product)
    def product_in_cart(self):
        return self.get_text(self.item_name)
    def compare_both(self):
        return self.selected_product()==self.product_in_cart()




