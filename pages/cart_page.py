class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_items = page.locator(".cart-item")
        self.cart_count = page.locator("#shop2-cart .cart-header__title span")

    def open(self):
        self.page.goto("https://aabs.pro/magazin/cart")

    def count_items(self):
        """Возвращает количество товаров в корзине (из счетчика)"""
        count_text = self.cart_count.text_content().strip()
        return int(count_text) if count_text.isdigit() else 0

    def is_product_in_cart(self, product_name):
        """Проверяет, есть ли товар в корзине (по названию или по счетчику)"""
        item_texts = [item.text_content() for item in self.cart_items.all()]
        return any(product_name in text for text in item_texts) or self.count_items() > 0
