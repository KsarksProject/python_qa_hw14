class ProductPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_button = page.locator(".shop-product-btn.type-3.buy")

    def open(self, url):
        """Открывает страницу конкретного товара"""
        self.page.goto(url)

    def add_to_cart(self):
        """Добавляет товар в корзину"""
        self.add_to_cart_button.click()
