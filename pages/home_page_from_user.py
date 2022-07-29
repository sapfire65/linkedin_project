import time
import pytest
from selenium import webdriver
from .base_page import BasePage
from .locators import HomePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

print('Напишите через пробел ключи поиска: ')
text_key = str(input()).lower().split()


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
        global text_key
        # Получаем количество в списке
        amount_elements = int(len(self.browser.find_elements(*HomePageLocators.STATUS_USER)))

        for i in range(1, amount_elements):
            first_window = self.browser.window_handles[0]  # переключается на первую вкладку

            # проверяем уровень сввязей
            number_level = self.browser.find_element(By.XPATH, f'(//span[@class="artdeco-entity-lockup__degree"])[{i}]').text
            if '2' in number_level:
                amount_elements_1 = self.browser.find_element(By.XPATH, f'(//div[@class="artdeco-entity-lockup__caption ember-view"])[{i}]').text
                amount_elements_1 = str(amount_elements_1).lower()
                print(amount_elements_1)

                # Поиск нужного ключа в статусе пользователя
                count = len(text_key)
                print(text_key)
                print(f'Количество ключей для поиска: {count}')
                for j in range(0, count):
                    print(text_key[j])
                    if text_key[j] in amount_elements_1:
                        atr = self.browser.find_element(By.XPATH, f'(//div[@class="inline-flex full-width"]//a)[{i}]')
                        atr_check = atr.get_attribute('href')
                        print(atr_check)
                        self.browser.execute_script("window.open('about:blank', 'tab2');")  # Открывает новую пустую вкладку
                        self.browser.switch_to.window('tab2')
                        self.browser.get(atr_check)
                        time.sleep(1)

                        # Проверка элемента '+', что бы не нажать на отслеживание ленты.
                        text_button_from_user = self.is_element_present(*HomePageLocators.ELEM_PLUS_BUTTON_FROM_USER)
                        print(f'ОТСЛЕЖИВАТЬ: {text_button_from_user}')
                        if text_button_from_user is True:
                            self.browser.execute_script('window.close()')  # Закрыть текущую вкладку
                            self.browser.switch_to.window(first_window)
                            break
                        elif text_button_from_user is False:
                            self.browser.find_element(By.XPATH, '//div[@class="pvs-profile-actions "]//span[@class="artdeco-button__text"]').click()
                            time.sleep(1)
                            self.browser.execute_script('window.close()')  # Закрыть текущую вкладку
                            self.browser.switch_to.window(first_window)
                        print('Есть совпадение')
                        break
                    else:
                        print('Нет совпадений')


















