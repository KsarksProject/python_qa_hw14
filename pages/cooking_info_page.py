import time
from selene import browser, have, by, command, be


class CookingInfoPage:

    def open_cooking_info(self):
        browser.element(by.text('Как мы готовим')).click()
        time.sleep(1)

    def check_cooking_title(self):
        browser.element('h1').should(have.text('Как мы готовим'))

    def check_cooking_content(self):
        browser.element('.cooking-content').should(be.visible)
        # Проверка наличия текста о приготовлении на гриле
        browser.element('.cooking-content').should(have.text('гриль'))

    def check_cooking_images(self):
        # Проверка наличия изображений в разделе
        browser.all('.cooking-images img').should(have.size_greater_than(0))

    def check_cooking_videos(self):
        # Проверка наличия видео в разделе (если они есть)
        browser.element('.cooking-videos').should(be.visible)

    def check_social_links(self):
        # Проверка наличия ссылок на социальные сети
        browser.element('.social-links').should(be.visible)

    def check_navigation_links(self):
        # Проверка наличия навигационных ссылок
        browser.all('.cooking-navigation a').should(have.size_greater_than(0))

    def click_first_recipe(self):
        # Клик по первому рецепту (если они есть)
        browser.element('.recipe-item').click()
        time.sleep(1)

    def check_recipe_details(self):
        # Проверка отображения деталей рецепта
        browser.element('.recipe-details').should(be.visible)
        browser.element('.recipe-ingredients').should(be.visible)
        browser.element('.recipe-steps').should(be.visible)