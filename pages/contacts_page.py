import time
from selene import browser, have, by, command, be


class ContactsPage:

    def open_contacts(self):
        browser.element(by.text('Контакты')).click()
        time.sleep(1)

    def check_contacts_title(self):
        browser.element('h1').should(have.text('Контакты'))

    def check_address(self):
        browser.element('.localcontacts__adress-inner').should(be.visible)
        browser.element('.localcontacts__adress-inner').should(have.text('г.Москва, Остаповский пр-д. д.11,с.4'))

    def check_phone(self):
        browser.element('a[href="tel:+79774797077"]').should(have.text('+7 (977) 479-70-77'))

    def check_working_hours(self):
        browser.element('.working-hours').should(have.text('9.00 до 22.00'))

    def check_map(self):
        browser.element('.map-container').should(be.visible)

    def fill_contact_form(self, name, email, message):
        browser.element('#input-name').type(name)
        browser.element('#input-email').type(email)
        browser.element('#input-enquiry').type(message)
        time.sleep(1)

    def submit_contact_form(self):
        browser.element('input[type="submit"]').click()
        time.sleep(2)

    def check_form_submission_success(self):
        browser.element('.alert-success').should(be.visible)

    def check_social_media_links(self):
        browser.element('.social-links').should(be.visible)
        # Проверка наличия ссылок на социальные сети
        browser.all('.social-links a').should(have.size_greater_than(0))