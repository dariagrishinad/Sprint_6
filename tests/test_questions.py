import allure
import pytest

from locators.locators_main_page import LocatorsMainPage
from page_object.main_page import MainPage


class TestQuestions:
    @allure.step('Тестирование блока "Вопросы о важном"')
    @pytest.mark.parametrize('question, answer, expected_answer', LocatorsMainPage.QUESTIONS_ANSWERS_EXPECTED)
    def test_click_on_question_text(self, driver, question, answer, expected_answer):

        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.accept_cookies()
        main_page.scroll()
        main_page.click_on_question(question)
        answer_text = main_page.get_answer_text(answer)

        assert answer_text == expected_answer
