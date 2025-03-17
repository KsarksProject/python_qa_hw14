from selene import browser, have, by, be
from selene.support.conditions import be as selene_be
from selene.support.shared import browser as selene_browser
from resources.product import Products
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MainPage:
    def open_browser(self):
        selene_browser.open("https://aabs.pro/")
        try:
            # Попытка найти и открыть попап поиска
            try:
                # Замените '.search-toggle' на реальный селектор триггера попапа
                search_trigger = selene_browser.element('.search-toggle')  # Уточните селектор!
                search_trigger.should(be.clickable).click()
            except Exception as e:
                print(f"Триггер попапа поиска не найден: {str(e)}. Попап может быть уже открыт.")

            # Ждем появления попапа и проверяем его видимость
            WebDriverWait(selene_browser.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "search-popup__inner"))
            )

            # Ждем появления поля поиска с name="search_text" и проверяем видимость
            search_element = WebDriverWait(selene_browser.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "search_text"))
            )
            search_element = selene_browser.element('[name="search_text"]')
            search_element.should(be.visible)  # Проверяем, что поле видно
            print("Поле поиска успешно найдено и отображается.")
        except Exception as e:
            print("Поле поиска с name='search_text' не найдено на странице или не отображается. HTML страницы:")
            print(selene_browser.driver.page_source)
            raise Exception("Поле поиска отсутствует на странице или не отображается. Тест не может продолжиться.")

    def check_main_menu(self):
        menu = selene_browser.element('[class="menu-default desktop-menu"]')
        menu.should(have.text("Главная"))
        menu.should(have.text("Видео"))
        menu.should(have.text("Фото"))
        menu.should(have.text("Кейтеринг"))
        menu.should(have.text("Как мы готовим"))
        menu.should(have.text("Эксклюзив от наших партнеров"))
        menu.should(have.text("Контакты"))

    def navigate_to_catalog(self):
        catalog_link = selene_browser.element(by.text("Кейтеринг"))
        catalog_link.should(be.clickable).click()
        WebDriverWait(selene_browser.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "site-main"))
        )

    def check_catalog_content(self):
        selene_browser.element('[class="site-main"]').should(be.visible)

    def add_to_cart_from_catalog(self):
        add_to_cart_button = selene_browser.element('[class="button-cart"]')
        add_to_cart_button.should(be.clickable).click()
        WebDriverWait(selene_browser.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn-inverse"))
        )

    def open_cart(self):
        cart_button = selene_browser.element('[class="btn-inverse"]')
        cart_button.should(be.clickable).click()
        WebDriverWait(selene_browser.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "table-responsive"))
        )

    def check_cart(self, value: Products):
        cart_table = selene_browser.element('[class="table-responsive"]')
        cart_table.should(have.text(value.model))
        cart_table.element('[class="quantity"]').should(have.text(value.quantity))

    def check_product_details(self, value: Products):
        product_layout = selene_browser.element('[class="product-layout"]')
        product_layout.should(be.clickable).click()
        WebDriverWait(selene_browser.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-info"))
        )
        product_info = selene_browser.element('[class="product-info"]')
        product_info.should(have.text(value.model))
        product_info.should(have.text(value.price))

    def perform_search(self, search_query):
        search_input = selene_browser.element('[name="search_text"]')
        search_input.should(be.visible).type(search_query)
        search_button = selene_browser.element('.search-block__btn')
        search_button.should(be.clickable).click()
        WebDriverWait(selene_browser.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-results"))
        )