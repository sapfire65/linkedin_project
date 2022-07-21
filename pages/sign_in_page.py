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
        self.messege_positive_check(f'Позитивная проверка валидации E-mail: alexandr.cherenkov.exlab@gmail.com')
        print()
        input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
        input_valid_email.send_keys('alexandr.cherenkov.exlab@gmail.com')
        self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
        amount = len(self.browser.find_elements(*SignInLocators.FEEDBACK_MESSAGE))
        assert amount == 1, 'Валидация E-mail провалена, появилось сообщение об ошибке.'


    def input_negative_email_test_1(self):
        self.messege_negative_check(f'Негативная проверка  E-mail: - пустое поле')
        print('')
        input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
        input_valid_email.click()
        self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
        time.sleep(5)

        amount = len(self.browser.find_elements(*SignInLocators.FEEDBACK_MESSAGE))
        if amount == 2:
            error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
            assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'
        else:
            assert amount == 2, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'


    def input_negative_email_test_2(self):
        self.messege_negative_check(f'Негативная проверка валидации E-mail: заглавные латинские буквы - "EXLAB@gmail.com"')
        print()
        input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
        input_valid_email.send_keys("EXLAB@gmail.com")
        self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
        time.sleep(1)
        amount = len(self.browser.find_elements(*SignInLocators.FEEDBACK_MESSAGE))
        if amount == 2:
            error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
            assert error_message == True, 'Валидация E-mail провалена, сообщение об ошибке не появилось.'
        else:
            assert amount == 2, 'Валидация E-mail провалена, имя почты заглавными буквами не допустимо.'


    def input_negative_email_test_3(self):
        self.messege_negative_check(f'Негативная проверка E-mail: Кириллица: "экслаб@gmail.com"')
        print()
        input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
        input_valid_email.send_keys("экслаб@gmail.com")
        self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
        time.sleep(1)
        amount = len(self.browser.find_elements(*SignInLocators.FEEDBACK_MESSAGE))
        if amount == 2:
            error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
            assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'
        else:
            assert amount == 2, 'Негативная проверка E-mail провалена, поле не должно принемать кириллицу.'


    def input_negative_email_test_4(self):
        self.messege_negative_check(f'Негативная проверка E-mail: только цифры - "1234567890@gmail.com"')
        print()
        input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
        input_valid_email.send_keys("1234567890@gmail.com")
        self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
        time.sleep(1)
        amount = len(self.browser.find_elements(*SignInLocators.FEEDBACK_MESSAGE))
        if amount == 2:
            error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
            assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'
        else:
            assert amount == 2, 'Негативная проверка E-mail провалена, имя почты не может состоять только из цифр.'


    def input_negative_email_test_5(self):
        self.messege_negative_check(f'Негативная проверка E-mail: иероглифы - "亚历山大@gmail.com"')
        print()
        input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
        input_valid_email.send_keys("亚历山大@gmail.com")
        self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
        time.sleep(1)
        amount = len(self.browser.find_elements(*SignInLocators.FEEDBACK_MESSAGE))
        if amount == 2:
            error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
            assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'
        else:
            assert amount == 2, 'Негативная проверка E-mail провалена, имя почты не может состоять только из иероглифов.'


    def input_negative_email_test_6(self):
        self.messege_negative_check(f'Негативная проверка E-mail: символы пунктуации - "-,@gmail.com"')
        print()
        input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
        input_valid_email.send_keys("-,@gmail.com")
        self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
        time.sleep(1)
        amount = len(self.browser.find_elements(*SignInLocators.FEEDBACK_MESSAGE))
        if amount == 2:
            error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
            assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'
        else:
            assert amount == 2, 'Негативная проверка E-mail провалена, имя почты не может состоять из тире и запятой.'


    def input_negative_email_test_7(self):
        self.messege_negative_check(f'Негативная проверка E-mail: пробел - " @gmail.com"')
        print()
        input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
        input_valid_email.send_keys(" @gmail.com")
        self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
        time.sleep(1)
        amount = len(self.browser.find_elements(*SignInLocators.FEEDBACK_MESSAGE))
        if amount == 2:
            error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
            assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'
        else:
            assert amount == 2, 'Негативная проверка E-mail провалена, имя почты не может состоять из пробела.'


    def input_negative_email_test_8(self):
        self.messege_negative_check(f'Негативная проверка E-mail: пробел в начале - " exlab@gmail.com"')
        print()
        input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
        input_valid_email.send_keys(" exlab@gmail.com")
        self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
        time.sleep(1)
        amount = len(self.browser.find_elements(*SignInLocators.FEEDBACK_MESSAGE))
        if amount == 2:
            error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
            assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'
        else:
            assert amount == 2, 'Негативная проверка E-mail провалена, поле не может принимать пробел перед именем почты.'


    def input_negative_email_test_9(self):
        self.messege_negative_check(f'Негативная проверка E-mail: пробел в конце - "exlab@gmail.com "')
        print()
        input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
        input_valid_email.send_keys("exlab@gmail.com ")
        self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
        time.sleep(1)
        amount = len(self.browser.find_elements(*SignInLocators.FEEDBACK_MESSAGE))
        if amount == 2:
            error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
            assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'
        else:
            assert amount == 2, 'Негативная проверка E-mail провалена, поле не может принимать пробел в конце почты.'


    def input_negative_email_test_10(self):
            self.messege_negative_check(f'Негативная проверка E-mail: пробел в середине - "ex lab@gmail.com"')
            print()
            input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
            input_valid_email.send_keys("ex lab@gmail.com")
            self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
            time.sleep(1)
            amount = len(self.browser.find_elements(*SignInLocators.FEEDBACK_MESSAGE))
            if amount == 2:
                error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
                assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'
            else:
                assert amount == 2, 'Негативная проверка E-mail провалена, поле не может принимать пробел между символами.'


    def input_negative_email_test_11(self):
            self.messege_negative_check(f'Негативная проверка E-mail: латинские буквы длины 1 - "e@gmail.com"')
            print()
            input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)
            input_valid_email.send_keys("e@gmail.com")
            self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
            time.sleep(1)
            amount = len(self.browser.find_elements(*SignInLocators.FEEDBACK_MESSAGE))
            if amount == 2:
                error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
                assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'
            else:
                assert amount == 2, 'Негативная проверка E-mail провалена, имя почты не может состоять из одного символа.'


    def input_negative_email_test_12(self):
            self.messege_positive_check(f'Позитивная проверка E-mail: латинские буквы длины 64 - "e * 54@gmail.com"')
            print()
            input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)

            input_valid_email.send_keys(('e'*54) + '@gmail.com')
            self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
            time.sleep(1)
            amount = len(self.browser.find_elements(*SignInLocators.FEEDBACK_MESSAGE))
            if amount == 1:
                error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
                assert error_message == True, 'Позитивная проверка E-mail провалена, сообщение может состоять из 64 символов'
            else:
                assert amount == 1, 'Позитивная проверка E-mail провалена, сообщение может состоять из 64 символов'


    def input_negative_email_test_13(self):
            self.messege_positive_check(f'Позитивная проверка E-mail: латинские буквы максимальной длины 128 - "e * 118 + @gmail.com"')
            print()
            input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)

            input_valid_email.send_keys(('e'*118) + '@gmail.com')
            self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
            time.sleep(1)
            amount = len(self.browser.find_elements(*SignInLocators.FEEDBACK_MESSAGE))
            if amount == 1:
                error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
                assert error_message == True, 'Позитивная проверка E-mail провалена, сообщение может состоять из 118 символов'
            else:
                assert amount == 1, 'Позитивная проверка E-mail провалена, сообщение может состоять из 118 символов'


    def input_negative_email_test_14(self):
            self.messege_negative_check(f'Негативная проверка E-mail: (ГЗ) латинские буквы длины 129 - "e * 119 + @gmail.com"')
            print()
            input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)

            input_valid_email.send_keys(('e'*119) + '@gmail.com')
            self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
            time.sleep(1)
            amount = len(self.browser.find_elements(*SignInLocators.FEEDBACK_MESSAGE))
            if amount == 2:
                error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
                assert error_message == True, 'Негативная проверка E-mail провалена, сообщение об ошибке не появилось.'
            else:
                assert amount == 2, 'Негативная проверка E-mail провалена, имя почты не может состоять 129 символа.'


    def input_negative_email_test_15(self):
            self.messege_positive_check(f'Позитивная проверка E-mail: (ГЗ) латинские буквы длины 127 - "e * 117 + @gmail.com"')
            print()
            input_valid_email = self.browser.find_element(*SignInLocators.INPUT_EMAIL)

            input_valid_email.send_keys(('e'*117) + '@gmail.com')
            self.browser.find_element(*SignInLocators.SUBMIT_BUTTON).click()
            time.sleep(1)
            amount = len(self.browser.find_elements(*SignInLocators.FEEDBACK_MESSAGE))
            if amount == 1:
                error_message = self.is_element_present(*SignInLocators.FEEDBACK_MESSAGE)
                assert error_message == True, 'Позитивная проверка E-mail провалена, сообщение может состоять из 127 символов'
            else:
                assert amount == 1, 'Позитивная проверка E-mail провалена, сообщение может состоять из 127 символов'


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

