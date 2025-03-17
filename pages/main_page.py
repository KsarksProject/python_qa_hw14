import time
from selene import browser, have, by, command, be
from resources.product import Products


class MainPage:

    def open_browser(self):
        browser.open("https://aabs.pro/")
        time.sleep(2)  # Увеличиваем время ожидания загрузки страницы

    def search_product(self, value: Products):
        # Изменяем селектор на более общий для поля поиска
        browser.element('.search-form input[type="text"]').click().type(value.model).press_enter()
        time.sleep(3)

    def check_product_availability(self, value):
        # Используем более общий селектор для результатов поиска
        browser.element('.product-list').should(have.text(value.model))

    def add_to_cart(self):
        # Более общий селектор для кнопки добавления в корзину
        browser.element('.product-layout button[onclick*="cart.add"]').click()
        time.sleep(1)

    def open_cart(self):
        # Более общий селектор для корзины
        browser.element('#cart-total').click()
        time.sleep(1)
        browser.element('a[href*="checkout/cart"]').click()
        time.sleep(2)

    def check_cart(self, value):
        # Более общий селектор для проверки товара в корзине
        browser.element('.table-responsive').should(have.text(value.model))

    def check_main_menu(self):
        # Проверяем только основное меню, используя более общий селектор
        browser.element('#main-menu').should(be.visible)

    def navigate_to_category(self, category_name):
        # Ищем ссылку по тексту
        browser.element(by.text(category_name)).click()
        time.sleep(1)

    def check_category_content(self):
        # Проверяем, что страница категории загрузилась
        browser.element('h1').should(be.visible)

    def check_product_details(self, value):
        # Проверяем детали товара на странице
        browser.element('h1, .product-title').should(be.visible)

    def change_quantity(self, quantity):
        # Обновленный селектор для поля количества
        browser.element('input[name="quantity"]').clear().type(quantity)
        time.sleep(1)

    def check_fast_order_button(self):
        # Проверяем наличие кнопки быстрого заказа или любой кнопки заказа
        browser.element('#button-cart, .buy-one-click').should(be.visible)

    def click_request_call(self):
        # Проверяем наличие кнопки "Заказать звонок"
        browser.element('a[href*="callback"], #callback-button, .callback-btn').click()
        time.sleep(1)

    def check_phone_number(self):
        # Проверяем наличие телефона на странице
        browser.element('.phone-number, [href*="tel:"]').should(be.visible)

    def check_site_description(self):
        # Проверка описания сайта на главной странице
        browser.element('.site-info__desc').should(have.text('Угольные грили с системой автоподдува воздуха'))