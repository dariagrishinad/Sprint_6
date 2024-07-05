from selenium.webdriver.common.by import By

from constants import Constants
from locators.locators_main_page import LocatorsMainPage


class LocatorsOrderPage:
    NAME_FIELD = (By.XPATH, ".//input[@placeholder = '* Имя']")
    LASTNAME_FIELD = (By.XPATH, ".//input[@placeholder = '* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']")
    STATION_FIELD = (By.XPATH, ".//input[@placeholder = '* Станция метро']")
    STATION_FIRST = (By.XPATH, ".//div[text() = 'Черкизовская']")
    STATION_SECOND = (By.XPATH, ".//div[text() = 'Бульвар Рокоссовского']")
    PHONE = (By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text() = 'Далее']")
    DATE_ORDER = (By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']")
    DATE_FIRST = (By.XPATH, ".//div[contains(@class, 'react-datepicker__day--005')]")
    DATE_SECOND = (By.XPATH, ".//div[contains(@class, 'react-datepicker__day--018')]")
    RENT_TERM = (By.XPATH, ".//div[text() = '* Срок аренды']")
    TERM_FIRST = (By.XPATH, ".//div[text() = 'трое суток']")
    TERM_SECOND = (By.XPATH, ".//div[text() = 'сутки']")
    COLOR_FIRST = (By.XPATH, ".//input[@id='black']/parent::label")
    COLOR_SECOND = (By.XPATH, ".//input[@id='grey']/parent::label")
    COMMENT = (By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']")
    COMPLETE_ORDER_BUTTON = (By.XPATH, ".//button[contains(@class, 'Button_Middle__1CSJM') and text() = 'Заказать']")
    MODAL_WINDOW = (By.XPATH, ".//div[@class = 'Order_ModalHeader__3FDaJ']")
    MODAL_AGREE_BUTTON = (By.XPATH, ".//button[text() = 'Да']")
    MODAL_ORDER_COMPLETE = (By.XPATH, './/div[text()[contains(.,"Заказ оформлен")]]')
    SCOOTER_LOGO = (By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']")
    YA_LOGO = (By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']")
    DZEN_HEADER = (By.ID, 'dzen-header')
    ORDER_DATA = [
        [LocatorsMainPage.TOP_ORDER_BUTTON, Constants.FIRST_USER[0], Constants.FIRST_USER[1], Constants.FIRST_USER[2], STATION_FIRST, Constants.FIRST_USER[3], DATE_FIRST, TERM_FIRST, COLOR_FIRST, Constants.FIRST_USER[4]],
        [LocatorsMainPage.MIDDLE_ORDER_BUTTON, Constants.SECOND_USER[0], Constants.SECOND_USER[1], Constants.SECOND_USER[2], STATION_SECOND, Constants.SECOND_USER[3], DATE_SECOND, TERM_SECOND, COLOR_SECOND, Constants.SECOND_USER[4]]
    ]





