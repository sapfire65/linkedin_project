import time
import pytest
from selenium import webdriver
from .pages.sign_in_page import SignIn
from .pages.locators import SignInLocators

def test_guest_button_sign_in_page(support_browser, open_location_home_page):
    # перемещаемся в новый класс .pages.sign_in_page
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.click_button_sign_in()


def test_email_positive(support_browser, open_location_sign_in_page):
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.input_positive_email_test()


def test_email_negative_empty_line(support_browser, open_location_sign_in_page):
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.input_negative_email_test_1()


@pytest.mark.xfail(reason = 'ВОЗМОЖНО: - регистрация заглавными буквами допустима')
def test_email_negative_capital_latin_letters(support_browser, open_location_sign_in_page):
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.input_negative_email_test_2()

def test_email_negative_cyrillic(support_browser, open_location_sign_in_page):
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.input_negative_email_test_3()

def test_email_negative_numbers(support_browser, open_location_sign_in_page):
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.input_negative_email_test_4()

@pytest.mark.xfail(reason='поле возможно поддерживает использование иероглифов')
def test_email_negative_hieroglyphs(support_browser, open_location_sign_in_page):
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.input_negative_email_test_5()

def test_email_negative_punctuation(support_browser, open_location_sign_in_page):
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.input_negative_email_test_6()

def test_email_negative_space(support_browser, open_location_sign_in_page):
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.input_negative_email_test_7()

@pytest.mark.xfail(reason='возможно поле ввода автоматически удаляет пробел перед именем почты')
def test_email_negative_space(support_browser, open_location_sign_in_page):
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.input_negative_email_test_8()

@pytest.mark.xfail(reason='возможно поле ввода автоматически удаляет пробел после почты')
def test_email_negative_space_to_end_text(support_browser, open_location_sign_in_page):
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.input_negative_email_test_9()

def test_email_negative_space_in_the_middle_of_the_ext(support_browser, open_location_sign_in_page):
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.input_negative_email_test_10()

def test_email_negative_one_latin_character(support_browser, open_location_sign_in_page):
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.input_negative_email_test_11()

def test_email_negative_54_latin_character(support_browser, open_location_sign_in_page):
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.input_negative_email_test_12()

def test_email_negative_128_latin_character(support_browser, open_location_sign_in_page):
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.input_negative_email_test_13()

def test_email_negative_129_latin_character(support_browser, open_location_sign_in_page):
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.input_negative_email_test_14()

def test_email_negative_127_latin_character(support_browser, open_location_sign_in_page):
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.input_negative_email_test_15()

def test_email_negative_experemental_1(support_browser, open_location_sign_in_page):
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.input_negative_email_test_16()


def test_email_negative_experemental_17(support_browser, open_location_sign_in_page):
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.input_negative_email_test_17()

def test_email_negative_experemental_18(support_browser, open_location_sign_in_page):
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.input_negative_email_test_18()


def test_email_negative_experemental_19(support_browser, open_location_sign_in_page):
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.input_negative_email_test_19()

def test_email_negative_experemental_20(support_browser, open_location_sign_in_page):
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.input_negative_email_test_20()

def test_email_negative_experemental_21(support_browser, open_location_sign_in_page):
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.input_negative_email_test_21()

def test_email_negative_experemental_22(support_browser, open_location_sign_in_page):
    sign_in_page = SignIn(support_browser, support_browser.current_url)
    sign_in_page.input_negative_email_test_22()


    # time.sleep(0)







