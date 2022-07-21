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

    # sign_in_page.input_negative_email_test_2()
    # sign_in_page.input_negative_email_test_3()
    # sign_in_page.input_negative_email_test_4()
    # sign_in_page.input_negative_email_test_5()
    # sign_in_page.input_negative_email_test_6()
    # sign_in_page.input_negative_email_test_7()
    # sign_in_page.input_negative_email_test_8()
    # sign_in_page.input_negative_email_test_9()
    # sign_in_page.input_negative_email_test_10()
    # sign_in_page.input_negative_email_test_11()
    # sign_in_page.input_negative_email_test_12()
    # sign_in_page.input_negative_email_test_13()
    # sign_in_page.input_negative_email_test_14()
    # sign_in_page.input_negative_email_test_15()
    # sign_in_page.input_negative_email_test_16()

    # time.sleep(0)

