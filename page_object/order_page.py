import allure

from constants import Urls
from locators.locators_order_page import LocatorsOrderPage
from page_object.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Нажать на селект выбора станции метро')
    def click_on_station_button(self):
        self.click_on_element(LocatorsOrderPage.STATION_FIELD)

    @allure.step('Нажать на кнопку "Далее"')
    def click_on_next_button(self):
        self.click_on_element(LocatorsOrderPage.NEXT_BUTTON)

    @allure.step('Выбор даты заказа')
    def click_on_date_order(self):
        self.click_on_element(LocatorsOrderPage.DATE_ORDER)

    @allure.step('Выбор периода аренды')
    def click_on_rent_term(self):
        self.click_on_element(LocatorsOrderPage.RENT_TERM)

    @allure.step('Заполнить инпут "Имя"')
    def fill_name_input(self, name):
        self.fill_input(name, LocatorsOrderPage.NAME_FIELD)

    @allure.step('Заполнить инпут "Фамилия"')
    def fill_lastname_input(self, lastname):
        self.fill_input(lastname, LocatorsOrderPage.LASTNAME_FIELD)

    @allure.step('Заполнить инпут "Адрес"')
    def fill_address_input(self, address):
        self.fill_input(address, LocatorsOrderPage.ADDRESS_FIELD)

    @allure.step('Заполнить инпут "Телефон"')
    def fill_phone_input(self, phone):
        self.fill_input(phone, LocatorsOrderPage.PHONE)

    @allure.step('Заполнить инпут "Комментарий"')
    def fill_comment_input(self, comment):
        self.fill_input(comment, LocatorsOrderPage.COMMENT)

    @allure.step('Нажать на кнопку "Заказать" после заполнения данных о заказе')
    def click_on_complete_button(self):
        self.click_on_element(LocatorsOrderPage.COMPLETE_ORDER_BUTTON)

    @allure.step('Проверка открытия модального окна с подтверждением заказа')
    def is_modal_window_open(self):
        return self.find_element_located(LocatorsOrderPage.MODAL_WINDOW)

    @allure.step('Кнопка согласия в модальном окне с подтверждением заказа')
    def click_on_agree_button(self):
        self.click_on_element(LocatorsOrderPage.MODAL_AGREE_BUTTON)

    @allure.step('Проверка открытия модального окна "Заказ оформлен"')
    def check_modal_complete_order(self):
        return self.find_element_located(LocatorsOrderPage.MODAL_ORDER_COMPLETE)

    @allure.step('Открытие страницы оформления заказа')
    def open_order_page(self):
        self.go_to_site(Urls.ORDER_PAGE_URL)

    @allure.step('Нажатие на логотип "Самокат"')
    def click_on_logo_scooter(self):
        self.click_on_element(LocatorsOrderPage.SCOOTER_LOGO)

    @allure.step('Нажатие на логотип "Яндекс"')
    def click_on_ya_logo(self):
        self.click_on_element(LocatorsOrderPage.YA_LOGO)

    @allure.step('Проверка нахождения хедера на Яндекс.Дзен')
    def check_dzen_header(self):
        return self.find_element_located(LocatorsOrderPage.DZEN_HEADER)
