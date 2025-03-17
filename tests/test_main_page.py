import allure
import pytest
from pages.main_page import MainPage
from resources.product import Products


@pytest.fixture
def main_page():
    return MainPage()


def test_dummy():
    assert 1 == 1


def test_main_page_search_and_cart(browser_set, main_page):
    with allure.step("Open the webpage"):
        try:
            main_page.open_browser()
        except Exception as e:
            pytest.fail(str(e))

    with allure.step("Perform search"):
        main_page.perform_search("гриль")  # Пример запроса

    with allure.step("Navigate to Кейтеринг"):
        main_page.navigate_to_catalog()

    with allure.step("Check Кейтеринг content"):
        main_page.check_catalog_content()

    with allure.step("Add product to cart"):
        main_page.add_to_cart_from_catalog()

    with allure.step("Open cart"):
        main_page.open_cart()

    with allure.step("Check cart contents"):
        product = Products()
        main_page.check_cart(product)


def test_main_page_navigation(browser_set, main_page):
    with allure.step("Open the webpage"):
        try:
            main_page.open_browser()
        except Exception as e:
            pytest.fail(str(e))

    with allure.step("Check main menu"):
        main_page.check_main_menu()

    with allure.step("Navigate to Кейтеринг"):
        main_page.navigate_to_catalog()

    with allure.step("Check Кейтеринг content"):
        main_page.check_catalog_content()


def test_product_details(browser_set, main_page):
    with allure.step("Open the webpage"):
        try:
            main_page.open_browser()
        except Exception as e:
            pytest.fail(str(e))

    with allure.step("Navigate to Кейтеринг"):
        main_page.navigate_to_catalog()

    with allure.step("Check product details"):
        product = Products()
        main_page.check_product_details(product)