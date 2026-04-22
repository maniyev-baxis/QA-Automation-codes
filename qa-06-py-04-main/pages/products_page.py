class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.title_heading = page.locator('[data-test="title"]')
        self.sauce_labs_backpack_add_to_cart_button = page.locator("#add-to-cart-sauce-labs-backpack")
        self.sauce_labs_bike_light_add_to_cart_button = page.locator("#add-to-cart-sauce-labs-bike-light")

    def visit(self):
        self.page.goto("https://www.saucedemo.com/inventory.html")

    def add_to_cart(self):
        self.sauce_labs_backpack_add_to_cart_button.click()

    def add_to_cart_item(self, item):
        item.click()