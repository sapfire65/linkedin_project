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
    time.sleep(3)

    # Свернуть чат
    hide_chat = HomePageFromUser(support_browser, support_browser.current_url)
    hide_chat.hide_chat()


