import time
import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from resources.product import product
from resources.user import test_user

mainpage = MainPage()
orderpage = OrderPage()


@allure.epic("Заказ товара")
@allure.feature("Оформление заказа")
def test_order_complete_flow(browser_set):
    # Шаг 1: Открытие страницы и добавление товара в корзину
    with allure.step("Открытие веб-страницы"):
        mainpage.open_browser()

    with allure.step("Открытие страницы угольного гриля"):
        browser_set.open("https://aabs.pro/electronic-control/coal-pilot-xx")
        time.sleep(1)

    with allure.step("Добавить товар в корзину"):
        mainpage.add_to_cart()
        time.sleep(1)

    with allure.step("Открываем корзину"):
        mainpage.open_cart()

    # Шаг 2: Переход к оформлению заказа и заполнение данных
    with allure.step("Переход к оформлению заказа"):
        orderpage.proceed_to_checkout()

    with allure.step("Заполнение данных покупателя"):
        orderpage.fill_customer_info(test_user)

    with allure.step("Выбор способа оплаты"):
        orderpage.select_payment_method("card")

    with allure.step("Выбор способа доставки"):
        orderpage.select_delivery_method("courier")

    # Шаг 3: Подтверждение заказа и проверка результата
    with allure.step("Подтверждение заказа"):
        orderpage.confirm_order()

    with allure.step("Проверка подтверждения заказа"):
        orderpage.check_order_confirmation()


@allure.epic("Заказ товара")
@allure.feature("Быстрый заказ")
def test_fast_order(browser_set):
    with allure.step("Открытие страницы угольного гриля"):
        browser_set.open("https://aabs.pro/electronic-control/coal-pilot-xx")
        time.sleep(1)

    with allure.step("Переход к быстрому заказу"):
        orderpage.go_to_fast_order()

    with allure.step("Заполнение формы быстрого заказа"):
        orderpage.fill_fast_order(test_user)

    with allure.step("Подтверждение быстрого заказа"):
        orderpage.confirm_fast_order()

    with allure.step("Проверка подтверждения быстрого заказа"):
        orderpage.check_fast_order_confirmation()


@allure.epic("Коммуникация")
@allure.feature("Обратный звонок")
def test_callback_request(browser_set):
    with allure.step("Открытие веб-страницы"):
        mainpage.open_browser()

    with allure.step("Клик по кнопке 'Заказать звонок'"):
        mainpage.click_request_call()

    with allure.step("Заполнение формы обратного звонка"):
        orderpage.fill_callback_form(test_user)

    with allure.step("Отправка формы обратного звонка"):
        orderpage.submit_callback_form()

    with allure.step("Проверка подтверждения запроса обратного звонка"):
        orderpage.check_callback_confirmation()


@allure.epic("Заказ товара")
@allure.feature("Изменение количества товара")
def test_quantity_change(browser_set):
    with allure.step("Открытие страницы угольного гриля"):
        browser_set.open("https://aabs.pro/electronic-control/coal-pilot-xx")
        time.sleep(1)

    with allure.step("Изменение количества товара на 3"):
        mainpage.change_quantity("3")

    with allure.step("Добавление товара в корзину"):
        mainpage.add_to_cart()
        time.sleep(1)

    with allure.step("Открытие корзины"):
        mainpage.open_cart()

    # Проверка количества в корзине - товаров должно быть 3
    with allure.step("Проверка количества товара в корзине"):
        product_with_new_quantity = product
        product_with_new_quantity.quantity = "3"
        mainpage.check_cart(product_with_new_quantity)