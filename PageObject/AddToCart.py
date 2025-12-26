from selenium.webdriver.common.by import By
from PageObject.base_page import BasePage

class AddToCart(BasePage):

    cart_icon = (By.XPATH,"//a[@class='shopping_cart_link']")
    item_name = (By.XPATH,"//div[@class='inventory_item_name']")
    remove_btn = (By.XPATH,"//button[contains(@id,'remove')]")
    click_chck_out = (By.XPATH, "//button[text()='Checkout']")

    def add_product_by_name(self,product_name):  # Build locator dynamically based on product name
        product_locator = ( By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button" )
        self.click(product_locator)

    def click_cart_icon(self):
        self.click(self.cart_icon)

    def validate_and_cleanup_cart(self):
        while True:
            items = [i.text.strip() for i in self.find_elements(self.item_name)]
            # Break when only Sauce Labs Onesie remains
            if all(name == "Sauce Labs Onesie" for name in items):
                break
    # Remove one unwanted item (not scoped properly in your version)
    # Better: find the remove button tied to that product
            for item in self.find_elements(self.item_name):
                if item.text.strip() != "Sauce Labs Onesie":
                    remove_btn = item.find_element( By.XPATH, "./ancestor::div[@class='cart_item']//button[contains(@id,'remove')]" )
                    remove_btn.click()
                    break
        self.click(self.click_chck_out)





