from selenium.webdriver.common.by import By

from constants import Constants


class LocatorsMainPage:
    QUESTIONS = [
        (By.ID, 'accordion__heading-0'),
        (By.ID, 'accordion__heading-1'),
        (By.ID, 'accordion__heading-2'),
        (By.ID, 'accordion__heading-3'),
        (By.ID, 'accordion__heading-4'),
        (By.ID, 'accordion__heading-5'),
        (By.ID, 'accordion__heading-6'),
        (By.ID, 'accordion__heading-7')
    ]
    ANSWERS = [
        (By.ID, 'accordion__panel-0'),
        (By.ID, 'accordion__panel-1'),
        (By.ID, 'accordion__panel-2'),
        (By.ID, 'accordion__panel-3'),
        (By.ID, 'accordion__panel-4'),
        (By.ID, 'accordion__panel-5'),
        (By.ID, 'accordion__panel-6'),
        (By.ID, 'accordion__panel-7')
    ]
    QUESTIONS_ANSWERS_EXPECTED = [
        [QUESTIONS[0], ANSWERS[0], Constants.ANSWERS_DATA[0]],
        [QUESTIONS[1], ANSWERS[1], Constants.ANSWERS_DATA[1]],
        [QUESTIONS[2], ANSWERS[2], Constants.ANSWERS_DATA[2]],
        [QUESTIONS[3], ANSWERS[3], Constants.ANSWERS_DATA[3]],
        [QUESTIONS[4], ANSWERS[4], Constants.ANSWERS_DATA[4]],
        [QUESTIONS[5], ANSWERS[5], Constants.ANSWERS_DATA[5]],
        [QUESTIONS[6], ANSWERS[6], Constants.ANSWERS_DATA[6]],
        [QUESTIONS[7], ANSWERS[7], Constants.ANSWERS_DATA[7]]
    ]
    TOP_ORDER_BUTTON = (By.XPATH, ".//div[@class = 'Header_Nav__AGCXC']/button[text() = 'Заказать']")
    MIDDLE_ORDER_BUTTON = (By.XPATH, ".//button[contains(@class, 'Button_Middle__1CSJM')]")
