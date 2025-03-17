import time
import allure
import pytest

from pages.main_page import MainPage
from pages.catalog_page import CatalogPage

mainpage = MainPage()
catalogpage = CatalogPage()


@allure.epic("Категория товаров")
@allure.feature("Проверка категории 'Электронное управление'")
def test_electronic_control_category(browser_set):
    with allure.step("Открытие веб-страницы"):
        mainpage.open_browser()

    with allure.step("Переход в категорию 'Электронное управление'"):
        catalogpage.open_electronic_control()

    with allure.step("Проверка заголовка категории"):
        catalogpage.check_category_title("Электронное управление")

    with allure.step("Проверка наличия товаров в категории"):
        product_count = catalogpage.get_products_count()
        assert product_count > 0, "В категории 'Электронное управление' нет товаров"
        allure.attach(str(product_count), 'product_count', allure.attachment_type.TEXT)


@allure.epic("Меню навигации")
@allure.feature("Переход по пунктам меню")
@pytest.mark.parametrize("menu_item", ["Видео", "Фото", "Кейтеринг", "Как мы готовим", "Контакты"])
def test_menu_navigation(browser_set, menu_item):
    with allure.step("Открытие веб-страницы"):
        mainpage.open_browser()

    with allure.step(f"Переход в раздел: {menu_item}"):
        catalogpage.select_menu_item(menu_item)
        allure.attach(menu_item, 'menu_item', allure.attachment_type.TEXT)

    # Если есть специфическая проверка для каждого раздела, здесь можно добавить
    # условную логику или отдельные методы проверки


@allure.epic("Страница товара")
@allure.feature("Проверка элементов страницы товара")
def test_product_page_elements(browser_set):
    with allure.step("Открытие страницы угольного гриля"):
        browser.open("https://aabs.pro/electronic-control/coal-pilot-xx")
        time.sleep(1)

    with allure.step("Проверка хлебных крошек"):
        catalogpage.check_breadcrumbs()

    with allure.step("Проверка характеристик угольного гриля"):
        catalogpage.check_grill_features()

    with allure.step("Проверка кнопок навигации между товарами"):
        catalogpage.check_prev_next_buttons()


@allure.epic("Категория товаров")
@allure.feature("Проверка категории 'Эксклюзив от наших партнеров'")
def test_exclusive_partners_category(browser_set):
    with allure.step("Открытие веб-страницы"):
        mainpage.open_browser()

    with allure.step("Переход в категорию 'Эксклюзив от наших партнеров'"):
        catalogpage.select_menu_item("Эксклюзив от наших партнеров")

    with allure.step("Проверка заголовка категории"):
        catalogpage.check_category_title("Эксклюзив от наших партнеров")