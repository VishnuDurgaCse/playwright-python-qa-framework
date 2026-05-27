from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.first_name = "[data-test='firstName']"
        self.last_name = "[data-test='lastName']"
        self.postal_code = "[data-test='postalCode']"
        self.continue_button = "[data-test='continue']"
        self.finish_button = "[data-test='finish']"
        self.complete_header = ".complete-header"

    def fill_checkout_info(self, first, last, postal):
        self.page.fill(self.first_name, first)
        self.page.fill(self.last_name, last)
        self.page.fill(self.postal_code, postal)

    def click_continue(self):
        self.page.click(self.continue_button)

    def click_finish(self):
        self.page.click(self.finish_button)

    def get_complete_message(self):
        return self.page.inner_text(self.complete_header)