import time
from selene import browser, have, by, command, be


class GrillDetailsPage:

    def open_grill_page(self, url):
        browser.open(url)
        time.sleep(1)

    def check_grill_title(self, expected_title):
        browser.element('h1').should(have.text(expected_title))

    def check_grill_price(self, expected_price):
        browser.element('.price').should(have.text(expected_price))

    def check_grill_availability(self):
        browser.element('.stock').should(have.text('В наличии'))

    def check_grill_description(self):
        browser.element('.tab-content').should(be.visible)
        browser.element('.tab-content').should(have.text('Гриль угольный'))

    def check_grill_features(self):
        browser.element('.features').should(have.text('автоподдува воздуха'))
        browser.element('.features').should(have.text('долго служит'))

    def check_related_products(self):
        browser.element('.related-products').should(be.visible)

    def open_image_gallery(self):
        browser.element('.thumbnail').click()
        time.sleep(1)

    def check_image_gallery(self):
        browser.element('.mfp-figure').should(be.visible)

    def close_image_gallery(self):
        browser.element('.mfp-close').click()
        time.sleep(1)

    def check_technical_specifications(self):
        # Переключение на вкладку "Характеристики" если она существует
        browser.element(by.text('Характеристики')).click()
        time.sleep(1)
        browser.element('.specifications').should(be.visible)

    def add_to_wishlist(self):
        browser.element('[data-original-title="Добавить в закладки"]').click()
        time.sleep(1)

    def check_wishlist_notification(self):
        browser.element('.alert-success').should(be.visible)
        browser.element('.alert-success').should(have.text('Вы добавили'))