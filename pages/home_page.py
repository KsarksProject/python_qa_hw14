class HomePage:
    def __init__(self, page):
        self.page = page
        self.search_box = page.locator("#shop2-text")
        self.search_button = page.locator(".search-btn.gr-button-1")
        self.search_icon = page.locator(".compact-panel__search")
        self.cookies_button = page.locator("button:has-text('Продолжить')")

    def open(self):
        self.page.goto("https://aabs.pro/")
        self.accept_cookies()

    def accept_cookies(self):
        """Закрывает всплывающее окно с согласием на cookies"""
        if self.cookies_button.is_visible():
            self.cookies_button.click()

    def open_search(self):
        """Открывает строку поиска, если она скрыта"""
        if self.search_icon.is_visible():
            self.search_icon.click()

    def search(self, query):
        """Выполняет поиск товара"""
        self.open_search()
        self.search_box.fill(query)
        self.search_button.click()
