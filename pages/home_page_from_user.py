import time
import pytest
from selenium import webdriver
from .base_page import BasePage
from .locators import HomePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class HomePageFromUser(BasePage):
    # Явное ожидание элемента после авторизации. Свернуть чат.
    def hide_chat(self):
        button_chat = WebDriverWait(self.browser, 50).until(EC.element_to_be_clickable((HomePageLocators.HIDE_CHAT_BUTTON)))
        button_chat.click()

    # Поиск поста
    def serch_post(self):
        elem_posts = WebDriverWait(self.browser, 50).until(EC.element_to_be_clickable((HomePageLocators.REACTION)))
        elem_posts.click()
        # проверяем что окно открылось
        window_like_ok = self.is_element_present(*HomePageLocators.WINDOW_LIKE_OK)
        print(window_like_ok)
        assert window_like_ok is True, 'Окно со списком лайкнувших, не найдено'

    def serch_specialization(self):
        # Получаем количество в списке
        amount_elements = int(len(self.browser.find_elements(*HomePageLocators.STATUS_USER)))

        for i in range(1, amount_elements + 1):
            # проверяем уровень сввязей
            number_level = self.browser.find_element(By.XPATH, f'(//span[@class="artdeco-entity-lockup__degree"])[{i}]').text
            if '2' in number_level:
                amount_elements_1 = self.browser.find_element(By.XPATH, f'(//div[@class="artdeco-entity-lockup__caption ember-view"])[{i}]').text
                print()
                print(amount_elements_1)











