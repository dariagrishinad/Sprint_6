import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Зайти на сайт')
    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    @allure.step('Проверить наличие элемента на сайте')
    def find_element_located(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    @allure.step('Кликнуть по кликабельному элементу')
    def click_on_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    # @allure.step('Принять куки')
    # def accept_cookies(self):
    #     return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LocatorsBasePage.COOKIES_BUTTON)).click()

    @allure.step('Проскроллить страницу')
    def scroll(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    @allure.step('Заполнить инпут')
    def fill_input(self, text, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)).send_keys(text)

    @allure.step('Получить url текущей страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Переход на новую открытую вкладку')
    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
