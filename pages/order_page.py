import time
from selene import browser, have, by, command, be
from resources.user import User


class OrderPage:

    def proceed_to_checkout(self):
        browser.element(by.text("Оформить заказ")).click()
        time.sleep(1)

    def fill_customer_info(self, user: User):
        browser.element('[name="name"]').click().type(user.name)
        browser.element('[name="email"]').click().type(user.email)
        browser.element('[name="phone"]').click().type(user.phone)
        browser.element('[name="address"]').click().type(user.address)
        time.sleep(1)

    def select_payment_method(self, method: str):
        browser.element(f'[name="payment_method"][value="{method}"]').click()
        time.sleep(1)

    def select_delivery_method(self, method: str):
        browser.element(f'[name="shipping_method"][value="{method}"]').click()
        time.sleep(1)

    def confirm_order(self):
        browser.element('[id="button-confirm"]').click()
        time.sleep(2)

    def check_order_confirmation(self):
        browser.element('[id="content"]').should(have.text('Ваш заказ сформирован'))

    def go_to_fast_order(self):
        browser.element(by.text("Быстрый заказ")).click()
        time.sleep(1)

    def fill_fast_order(self, user: User):
        browser.element('[name="name"]').click().type(user.name)
        browser.element('[name="phone"]').click().type(user.phone)
        time.sleep(1)

    def confirm_fast_order(self):
        browser.element('[id="fast-order-submit"]').click()
        time.sleep(2)

    def check_fast_order_confirmation(self):
        browser.element('[class="success-message"]').should(be.visible)

    def fill_callback_form(self, user: User):
        browser.element('[name="callback-name"]').click().type(user.name)
        browser.element('[name="callback-phone"]').click().type(user.phone)
        time.sleep(1)

    def submit_callback_form(self):
        browser.element('[id="callback-submit"]').click()
        time.sleep(2)

    def check_callback_confirmation(self):
        browser.element('[class="callback-confirmation"]').should(be.visible)