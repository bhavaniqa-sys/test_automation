from PageObject.Login import LoginPage
from PageObject.AddToCart import AddToCart
from PageObject.checkout import Checkout
from PageObject.Menu import MenuPage
import json

def test_end_to_end(driver,user_data,product_data):
    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.enter_username(user_data["username"])
    login_page.enter_password(user_data["password"])
    login_page.click_login()

    cart_page = AddToCart(driver)
    # Step 2: Add all products from JSON
    for product_name in product_data:
        cart_page.add_product_by_name(product_name)
    cart_page.click_cart_icon()
    cart_page.validate_and_cleanup_cart()

    # Step 3 : Checkout the item
    chck_out = Checkout(driver)
    chck_out.enter_first_name(user_data["firstname"])
    chck_out.enter_last_name(user_data["lastname"])
    chck_out.enter_zip_code(user_data["zipcode"])
    chck_out.continue_button()
    chck_out.finish_button()
    assert chck_out.confirm_msg_text(),"Thank you message"

    # Step 4: Logout
    menu_page = MenuPage(driver)
    menu_page.open_menu()
    menu_page.click_logout()



