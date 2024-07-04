import allure
import pytest

from constants import Urls
from locators.locators_order_page import LocatorsOrderPage
from page_object.main_page import MainPage
from page_object.order_page import OrderPage


class TestOrder:
    @allure.step('Тестирование заказа самоката с двумя наборами тестовых данных')
    @pytest.mark.parametrize('button, name, lastname, address, station, phone, order_date, rent_term, color, comment', LocatorsOrderPage.ORDER_DATA)
    def test_order(self, driver, button, name, lastname, address, station, phone, order_date, rent_term, color, comment):
        main_page = MainPage(driver)
        main_page.go_to_site(Urls.MAIN_URL)
        main_page.accept_cookies()
        main_page.click_on_order_button(button)
        order_page = OrderPage(driver)
        order_page.fill_name_input(name)
        order_page.fill_lastname_input(lastname)
        order_page.fill_address_input(address)
        order_page.click_on_station_button()
        order_page.click_on_element(station)
        order_page.fill_phone_input(phone)
        order_page.click_on_next_button()
        order_page.click_on_date_order()
        order_page.click_on_element(order_date)
        order_page.click_on_rent_term()
        order_page.click_on_element(rent_term)
        order_page.click_on_element(color)
        order_page.fill_comment_input(comment)
        order_page.click_on_complete_button()
        order_page.is_modal_window_open()
        order_page.click_on_agree_button()

        assert order_page.check_modal_complete_order()

    @allure.step('Проверка перехода на главную страницу при клике на логотип "Самокат"')
    def test_click_on_logo_scooter(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.click_on_logo_scooter()

        assert order_page.get_current_url() == Urls.MAIN_URL

    @allure.step('Проверка перехода на страницу "Яндекс.Дзен" при клике на логотип "Яндекс"')
    def test_click_on_ya_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.click_on_ya_logo()
        order_page.switch_to_window()
        order_page.check_dzen_header()

        assert order_page.get_current_url() == Urls.DZEN_URL
