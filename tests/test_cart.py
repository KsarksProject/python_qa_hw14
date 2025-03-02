import allure
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@allure.feature("Корзина")
@allure.story("Добавление товара в корзину")
def test_add_specific_product_to_cart(browser):
    home_page = HomePage(browser)
    product_page = ProductPage(browser)
    cart_page = CartPage(browser)

    with allure.step("Открываем сайт и выполняем поиск товара"):
        home_page.open()
        home_page.search("Гриль угольный нового поколения Coal Pilot XX")

    with allure.step("Открываем страницу товара"):
        product_page.open("https://aabs.pro/magazin/product/gril-ugolnyj-coal-pilot-xx")

    with allure.step("Добавляем товар в корзину"):
        product_page.add_to_cart()

    with allure.step("Открываем корзину и проверяем, что товар добавлен"):
        cart_page.open()
        assert cart_page.is_product_in_cart("Гриль угольный нового поколения Coal Pilot XX"), "Товар отсутствует в корзине"
