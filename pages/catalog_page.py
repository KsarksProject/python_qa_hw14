import time
from selene import browser, have, by, command, be


class CatalogPage:

    def open_electronic_control(self):
        browser.element(by.text('Электронное управление')).click()
        time.sleep(1)

    def check_category_title(self, category_name):
        browser.element('h1').should(have.text(category_name))

    def filter_by_price(self, min_price, max_price):
        # Предполагаем наличие фильтра по цене на сайте
        browser.element('[data-min-price]').clear().type(str(min_price))
        browser.element('[data-max-price]').clear().type(str(max_price))
        browser.element('[data-filter-button]').click()
        time.sleep(2)

    def sort_by(self, sort_option):
        # Предполагаем наличие сортировки на сайте
        browser.element('[data-sort-select]').click()
        browser.element(by.text(sort_option)).click()
        time.sleep(2)

    def select_menu_item(self, menu_item):
        browser.element(by.text(menu_item)).click()
        time.sleep(1)

    def get_products_count(self):
        return len(browser.all('[class="product-layout"]'))

    def check_price_in_range(self, min_price, max_price):
        prices = browser.all('.price').get(have.texts)

        # Преобразуем текстовые цены в числа
        numeric_prices = []
        for price_text in prices:
            # Удаляем все нечисловые символы, кроме точки
            clean_price = ''.join(c for c in price_text if c.isdigit() or c == '.')
            numeric_prices.append(float(clean_price))

        # Проверяем, что все цены в заданном диапазоне
        all_in_range = all(min_price <= price <= max_price for price in numeric_prices)
        return all_in_range

    def check_grill_features(self):
        # Проверка характеристик угольного гриля
        browser.element('[class="product-info"]').should(have.text('угольный'))
        browser.element('[class="product-info"]').should(have.text('автоподдува'))

    def check_breadcrumbs(self):
        # Проверка хлебных крошек
        browser.element('.breadcrumb').should(have.text('Главная'))
        browser.element('.breadcrumb').should(have.text('Электронное управление'))

    def check_prev_next_buttons(self):
        # Проверка кнопок предыдущий/следующий товар
        browser.element(by.text('Предыдущий товар')).should(be.visible)
        browser.element(by.text('Следующий товар')).should(be.visible)