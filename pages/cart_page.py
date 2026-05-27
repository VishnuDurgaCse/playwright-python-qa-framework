from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_container = "#cart_contents_container"
        self.checkout_button = "[data-test='checkout']"
        self.cart_item = ".cart_item"

    def is_cart_page(self):
        return self.page.is_visible(self.cart_container)

    def get_cart_items(self):
        return self.page.locator(self.cart_item).count()

    def proceed_to_checkout(self):
        self.page.click(self.checkout_button)