import allure
from pages.home_page import HomePage

@allure.feature("Главная страница")
@allure.story("Открытие сайта")
def test_open_homepage(browser):
    """Тест открывает главную страницу интернет-магазина"""
    home_page = HomePage(browser)
    with allure.step("Открываем главную страницу и принимаем cookies"):
        home_page.open()
    with allure.step("Проверяем, что главная страница загрузилась"):
        assert "AABS Угольные грили с системой автоматического поддува воздуха" in browser.title(), "Главная страница не загрузилась"
