import allure
from pages.login_page import LoginPage


@allure.feature("Авторизация")
@allure.story("Успешный вход в систему")
def test_successful_login(browser):
    """Тест проверяет успешную авторизацию"""
    login_page = LoginPage(browser)

    with allure.step("Открываем главную страницу"):
        login_page.open()

    with allure.step("Открываем модальное окно входа"):
        login_page.open_login_modal()

    with allure.step("Выполняем вход"):
        login_page.login()

    with allure.step("Открываем профиль через 'Кабинет'"):
        assert login_page.open_profile(), "Ошибка: ссылка на профиль 'Ksark' не найдена"

    with allure.step("Проверяем, что авторизация успешна"):
        assert login_page.is_logged_in(), "Ошибка входа: пользователь не авторизован"
