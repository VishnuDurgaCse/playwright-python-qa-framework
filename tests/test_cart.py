from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_product_to_cart(page):
    login = LoginPage(page)
    login.navigate_to_login()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.add_product_to_cart()
    inventory.go_to_cart()
    cart = CartPage(page)
    assert cart.is_cart_page(), "Cart page not visible"
    assert cart.get_cart_items() == 1, "Product not added to cart"

def test_cart_is_empty_on_fresh_login(page):
    login = LoginPage(page)
    login.navigate_to_login()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.go_to_cart()
    cart = CartPage(page)
    assert cart.get_cart_items() == 0, "Cart should be empty on fresh login"