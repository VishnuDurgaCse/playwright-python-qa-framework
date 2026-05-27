from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_complete_checkout(page):
    login = LoginPage(page)
    login.navigate_to_login()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.add_product_to_cart()
    inventory.go_to_cart()
    cart = CartPage(page)
    cart.proceed_to_checkout()
    checkout = CheckoutPage(page)
    checkout.fill_checkout_info("Vishnu", "Durga", "600001")
    checkout.click_continue()
    checkout.click_finish()
    message = checkout.get_complete_message()
    assert "Thank you for your order" in message

def test_checkout_without_firstname(page):
    login = LoginPage(page)
    login.navigate_to_login()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.add_product_to_cart()
    inventory.go_to_cart()
    cart = CartPage(page)
    cart.proceed_to_checkout()
    checkout = CheckoutPage(page)
    checkout.fill_checkout_info("", "Durga", "600001")
    checkout.click_continue()
    assert page.is_visible("[data-test='error']"), "Error not shown for missing first name"