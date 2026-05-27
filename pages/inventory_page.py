from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.inventory_container = "#inventory_container"
        self.add_to_cart_button = "[data-test='add-to-cart-sauce-labs-backpack']"
        self.cart_icon = ".shopping_cart_link"
        self.menu_button = "#react-burger-menu-btn"
        self.logout_link = "#logout_sidebar_link"

    def is_inventory_page(self):
        return self.page.is_visible(self.inventory_container)

    def add_product_to_cart(self):
        self.page.click(self.add_to_cart_button)

    def go_to_cart(self):
        self.page.click(self.cart_icon)

    def logout(self):
        self.page.click(self.menu_button)
        self.page.click(self.logout_link)