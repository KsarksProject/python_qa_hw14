import time
import allure

from pages.contacts_page import ContactsPage

contactspage = ContactsPage()


@allure.epic("Информационные разделы")
@allure.feature("Страница 'Контакты'")
def test_contacts_page_info(browser_set):
    with allure.step("Открытие страницы 'Контакты'"):
        contactspage.open_contacts()

    with allure.step("Проверка заголовка страницы"):
        contactspage.check_contacts_title()

    with allure.step("Проверка адреса"):
        contactspage.check_address()

    with allure.step("Проверка телефона"):
        contactspage.check_phone()

    with allure.step("Проверка часов работы"):
        contactspage.check_working_hours()


@allure.epic("Информационные разделы")
@allure.feature("Карта на странице 'Контакты'")
def test_contacts_map(browser_set):
    with allure.step("Открытие страницы 'Контакты'"):
        contactspage.open_contacts()

    with allure.step("Проверка наличия карты"):
        contactspage.check_map()


@allure.epic("Информационные разделы")
@allure.feature("Форма обратной связи на странице 'Контакты'")
def test_contact_form(browser_set):
    with allure.step("Открытие страницы 'Контакты'"):
        contactspage.open_contacts()

    with allure.step("Заполнение формы обратной связи"):
        contactspage.fill_contact_form(
            name="Иван Тестовый",
            email="test@example.com",
            message="Это тестовое сообщение для проверки формы обратной связи"
        )

    with allure.step("Отправка формы"):
        contactspage.submit_contact_form()

    with allure.step("Проверка успешной отправки формы"):
        contactspage.check_form_submission_success()


@allure.epic("Информационные разделы")
@allure.feature("Ссылки на социальные сети на странице 'Контакты'")
def test_contacts_social_links(browser_set):
    with allure.step("Открытие страницы 'Контакты'"):
        contactspage.open_contacts()

    with allure.step("Проверка ссылок на социальные сети"):
        contactspage.check_social_media_links()