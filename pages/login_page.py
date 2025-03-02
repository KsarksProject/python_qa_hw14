import os
from dotenv import load_dotenv

load_dotenv()

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.base_url = os.getenv("BASE_URL")
        self.login_modal_button = page.locator(".cabinet-block__btn")
        self.login_modal = page.locator(".remodal[data-remodal-id='cabinet-modal']")
        self.email_input = page.locator("#login")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button.gr-button-1", has_text="Войти")
        self.profile_menu = page.get_by_role("banner").get_by_text("Кабинет")
        self.logged_in_text = page.get_by_text("Вы вошли как:")
        self.profile_link = page.get_by_role("link", name="Ksark")

    def open(self):
        """Открывает главную страницу"""
        self.page.goto(self.base_url)

    def open_login_modal(self):
        """Открывает модальное окно входа"""
        if self.login_modal.is_visible():
            return  # Если окно уже открыто — пропускаем шаг

        self.login_modal_button.click(force=True)  # Принудительно кликаем
        self.page.wait_for_selector(".remodal-is-opened", state="visible", timeout=5000)

    def login(self):
        """Выполняет вход, используя данные из .env"""
        email = os.getenv("LOGIN")
        password = os.getenv("PASSWORD")

        self.open_login_modal()
        self.email_input.wait_for(state="visible")
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def is_logged_in(self):
        """Проверяет, успешен ли вход (по тексту 'Вы вошли как:')"""
        return self.logged_in_text.is_visible()

    def open_profile(self):
        """Открывает меню 'Кабинет' и проверяет ссылку на профиль"""
        self.profile_menu.click()
        return self.profile_link.is_visible()
