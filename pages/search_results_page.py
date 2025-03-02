class SearchResultsPage:
    def __init__(self, page):
        self.page = page
        self.search_results = page.locator(".product-item")

    def get_first_result_text(self):
        return self.search_results.nth(0).text_content().lower()

    def count_results(self):
        return self.search_results.count()
