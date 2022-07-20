import time
import pytest
from mimesis import Person
from mimesis.locales import Locale
from .base_page import BasePage
from .locators import SignInLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

count = 0

class SignIn(BasePage):

# Тестирование полей ввода login / pass
    def click_button_sign_in(self):
        global count
        self.is_header('Проверка клика по кнопке SignIn')
        button = self.browser.find_element(*SignInLocators.SIGN_IN_BUTTON)
        button.click()
        url_sign_in_page = self.browser.current_url
        print(f'\n{count + 1}) Проверка URL страницы SignIn после клика')
        count += 1
        print(f'Ожидаемый результат: {SignInLocators.LINC_LOCATION_SIGN_IN_PAGE}')
        print(f'Фактический результат: {url_sign_in_page}')
        assert SignInLocators.LINC_LOCATION_SIGN_IN_PAGE == url_sign_in_page, 'Это не страница авторизации'


    def input_positive_email_test(self):
        self.messege_positive_check(f'Позитивная проверка E-mail: alexandr.cherenkov.exlab@gmail.com')
        print()
        input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
        input_valid_email.send_keys('alexandr.cherenkov.exlab@gmail.com')
        time.sleep(1)
        self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
        error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
        time.sleep(3)
        assert error_message is True, 'Позитивная проверка E-mail провалена, появилось сообщение об ошибке.'

    def input_negative_email_test(self):
        self.messege_negative_check(f'Негативная проверка E-mail: alexandr.cherenkov.exlab@gmail.com')
