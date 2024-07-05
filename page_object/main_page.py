import allure

from constants import Urls
from locators.locators_main_page import LocatorsMainPage
from page_object.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Кликнуть на вопрос в блоке "Вопросы о важном"')
    def click_on_question(self, question):
        return self.click_on_element(question)

    @allure.step('Получить текст ответа в блоке "Вопросы о важном"')
    def get_answer_text(self, answer):
        return self.find_element_located(answer).text

    @allure.step('Нажать на кнопку "Заказать"')
    def click_on_order_button(self, button):
        self.click_on_element(button)

    @allure.step('Перейти на главную страницу сайта')
    def go_to_main_page(self):
        self.go_to_site(Urls.MAIN_URL)

    @allure.step('Принять куки')
    def accept_cookies(self):
        self.click_on_element(LocatorsMainPage.COOKIES_BUTTON)
