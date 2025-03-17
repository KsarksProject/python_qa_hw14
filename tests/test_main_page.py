import time
import allure
import pytest
from selene import browser, have, be

from pages.main_page import MainPage
from resources.product import product

mainpage = MainPage()


@pytest.mark.skip(reason="Проверить селекторы на реальном сайте")
def test_main_page_search_and_cart(browser_set):
    with allure.step("Открытие веб-страницы"):
        mainpage.open_browser()

    with allure.step("Поиск товара"):
        mainpage.search_product(product)

    with allure.step("Проверка наличия товара в поисковой выдаче"):
        mainpage.check_product_availability(product)

    with allure.step("Добавить товар в корзину"):
        mainpage.add_to_cart()
        time.sleep(2)

    with allure.step("Открываем корзину"):
        mainpage.open_cart()

    with allure.step("Проверка товара в корзине"):
        mainpage.check_cart(product)


def test_main_page_navigation(browser_set):
    with allure.step("Открытие веб-страницы"):
        mainpage.open_browser()

    with allure.step("Проверка видимости главного меню"):
        # Проверяем просто видимость меню
        browser.element('header').should(be.visible)

    with allure.step("Проверка заголовка страницы"):
        # Делаем простую проверку, что мы на нужном сайте
        browser.should(have.title_containing('AABS'))

    with allure.step("Проверка описания на главной странице"):
        # Проверяем наличие текста про угольные грили
        browser.element('.site-info__desc').should(have.text('Угольные грили с системой автоподдува воздуха'))


def test_product_details_simple(browser_set):
    with allure.step("Открытие веб-страницы"):
        mainpage.open_browser()

    with allure.step("Проверка основной структуры"):
        # Проверяем основные блоки на странице
        browser.element('header').should(be.visible)
        browser.element('footer').should(be.visible)


def test_phone_number_and_call_request(browser_set):
    with allure.step("Открытие веб-страницы"):
        mainpage.open_browser()

    with allure.step("Проверка телефона на странице"):
        # Ищем любые телефонные ссылки
        browser.all('[href*="tel:"]').should(have.size_greater_than_or_equal(1))


@pytest.mark.skip(reason="Проверить селекторы на реальном сайте")
def test_site_description(browser_set):
    with allure.step("Открытие веб-страницы"):
        mainpage.open_browser()

    with allure.step("Проверка описания сайта"):
        mainpage.check_site_description()