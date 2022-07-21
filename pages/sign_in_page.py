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
        self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
        amount = len(self.browser.find_elements(*SignInLocators.FEEDBACK_MESSAGE))
        assert amount == 1, 'Позитивная проверка E-mail провалена, появилось сообщение об ошибке.'


    def input_negative_email_test_1(self):
        self.messege_negative_check(f'Негативная проверка E-mail: - пустое поле')
        print()
        input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
        input_valid_email.click()
        self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
        time.sleep(1)
        error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
        assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'


    def input_negative_email_test_2(self):
        self.messege_negative_check(f'Негативная проверка E-mail: заглавные латинские буквы - "EXLAB"')
        print()
        input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
        input_valid_email.send_keys("EXLAB")
        self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
        time.sleep(1)
        error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
        assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'


    def input_negative_email_test_3(self):
        self.messege_negative_check(f'Негативная проверка E-mail: Кириллица: "экслаб"')
        print()
        input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
        input_valid_email.send_keys("экслаб")
        self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
        time.sleep(1)
        error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
        assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'


    def input_negative_email_test_4(self):
        self.messege_negative_check(f'Негативная проверка E-mail: цифры - "1234567890"')
        print()
        input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
        input_valid_email.send_keys("1234567890")
        self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
        time.sleep(1)
        error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
        assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'


    def input_negative_email_test_5(self):
        self.messege_negative_check(f'Негативная проверка E-mail: иероглифы - "亚历山大"')
        print()
        input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
        input_valid_email.send_keys("亚历山大")
        self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
        time.sleep(1)
        error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
        assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'


    def input_negative_email_test_6(self):
        self.messege_negative_check(f'Негативная проверка E-mail: символы пунктуации - "-,"')
        print()
        input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
        input_valid_email.send_keys("-,")
        self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
        time.sleep(1)
        error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
        assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'


    def input_negative_email_test_7(self):
        self.messege_negative_check(f'Негативная проверка E-mail: пробел - " "')
        print()
        input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
        input_valid_email.send_keys(" ")
        self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
        time.sleep(1)
        error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
        assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'


    def input_negative_email_test_8(self):
        self.messege_negative_check(f'Негативная проверка E-mail: пробел в начале - " exlab"')
        print()
        input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
        input_valid_email.send_keys(" exlab")
        self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
        time.sleep(1)
        error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
        assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'


    def input_negative_email_test_9(self):
        self.messege_negative_check(f'Негативная проверка E-mail: пробел в конце - "exlab "')
        print()
        input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
        input_valid_email.send_keys("exlab ")
        self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
        time.sleep(1)
        error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
        assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'



    def input_negative_email_test_10(self):
            self.messege_negative_check(f'Негативная проверка E-mail: пробел в середине - "ex lab "')
            print()
            input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
            input_valid_email.send_keys("ex lab ")
            self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
            time.sleep(1)
            error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
            assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'


    def input_negative_email_test_11(self):
            self.messege_negative_check(f'Негативная проверка E-mail: латинские буквы длины 1 - "e"')
            print()
            input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
            input_valid_email.send_keys("e")
            self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
            time.sleep(1)
            error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
            assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'


    def input_negative_email_test_12(self):
            self.messege_negative_check(f'Негативная проверка E-mail: латинские буквы длины 64 - "e * 64"')
            print()
            input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)

            input_valid_email.send_keys('e'*64)
            self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
            time.sleep(1)
            error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
            assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'


    def input_negative_email_test_13(self):
            self.messege_negative_check(f'Негативная проверка E-mail: латинские буквы максимальной длины 128 - "e * 128"')
            print()
            input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)

            input_valid_email.send_keys('e'*128)
            self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
            time.sleep(1)
            error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
            assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'


    def input_negative_email_test_14(self):
            self.messege_negative_check(f'Негативная проверка E-mail: (ГЗ) латинские буквы длины 129 - "e * 129"')
            print()
            input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)

            input_valid_email.send_keys('e'*129)
            self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
            time.sleep(1)
            error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
            assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'


    def input_negative_email_test_15(self):
            self.messege_negative_check(f'Негативная проверка E-mail: (ГЗ) латинские буквы длины 127 - "e * 127"')
            print()
            input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)

            input_valid_email.send_keys('e'*127)
            self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
            time.sleep(1)
            error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
            assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'


    def input_negative_email_test_16(self):
            self.messege_negative_check(f'Негативная проверка E-mail: составные варианты - "exlab@gmail"')
            print()
            input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)

            input_valid_email.send_keys('exlab@gmail')
            self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
            time.sleep(1)
            if len(self.browser.find_elements(*SignInLocators.FEEDBACK_MESSAGE)) == 2:
                error_message = True
            else:
                error_message = False

            assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'
