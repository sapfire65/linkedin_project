import time
import pytest
from selenium import webdriver
from .pages.locators import SignInLocators
from .pages.base_page import BasePage
from .pages.login_page import  LoginPage
from .pages.home_page_from_user import HomePageFromUser

def test_invite(support_browser, open_location_home_page):

    # Авторизация
    auth = BasePage(support_browser, support_browser.current_url)
    auth.user_authorization()

    # Свернуть чат
    home = HomePageFromUser(support_browser, support_browser.current_url)
    home.hide_chat()

    # Поиск поста / открыть список лайкнувших
    home.serch_post()


    time.sleep(5)


