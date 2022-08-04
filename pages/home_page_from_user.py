import time
import pytest
import re
from selenium import webdriver
from .base_page import BasePage
from .locators import HomePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *



print('Напишите через пробел ключи поиска: ')
text_key = str(input()).lower().split()

class HomePageFromUser(BasePage):
    # Явное ожидание элемента после авторизации. Свернуть чат.
    def hide_chat(self):
        button_chat = WebDriverWait(self.browser, 50).until(EC.element_to_be_clickable((HomePageLocators.HIDE_CHAT_BUTTON)))
        button_chat.click()

    # Поиск поста
    def serch_post(self):
        global text_key
        script_stopped = False

        while not script_stopped:
            for x in range(1, 500, 3):

                if self.is_element_present(By.XPATH, f'(//span[@class="social-details-social-counts__social-proof-container"])[{x}]'):
                    elem_posts = WebDriverWait(self.browser, 50).until(EC.element_to_be_clickable((By.XPATH, f'(//span[@class="social-details-social-counts__social-proof-container"])[{x}]')))
                    elem_posts.click()
                else:
                    for _ in range(3):
                        self.browser.execute_script('window.scrollBy(0, 300);')
                        return

                # проверяем что окно открылось
                window_like_ok = self.is_element_present(*HomePageLocators.WINDOW_LIKE_OK)
                assert window_like_ok is True, 'Окно со списком лайкнувших, не найдено'

                # Получаем количество лайкнувших в списке
                # count_st = len(self.browser.find_elements(By.XPATH, '//div[@class="artdeco-entity-lockup__caption ember-view"]'))
                # print(count_st)
                count = True

                while count:
                    count_st = len(self.browser.find_elements(By.XPATH, '//div[@class="artdeco-entity-lockup__caption ember-view"]'))
                    if self.is_element_present(By.XPATH, f'(//div[@class="artdeco-entity-lockup__caption ember-view"])[{count_st}]'):
                        move_to_the_object_in_widow = self.browser.find_element(By.XPATH, f'(//div[@class="artdeco-entity-lockup__caption ember-view"])[{count_st}]')
                        self.browser.execute_script("return arguments[0].scrollIntoView();", move_to_the_object_in_widow)
                        time.sleep(2)
                        count = self.explicit_element_wait(*HomePageLocators.LATER_RESULT)

                        if count is True:
                            try:
                                self.browser.find_element(*HomePageLocators.LATER_RESULT).click()
                                print(count)
                            except BaseException:
                                pass
                                count = False
                                print(count)
                                break

                # Получаем количество лайкнувших в списке
                amount_elements = int(len(self.browser.find_elements(*HomePageLocators.STATUS_USER)))
                for i in range(1, amount_elements + 1):
                    # проверяем уровень сввязей
                    number_level = self.browser.find_element(By.XPATH, f'(//span[@class="artdeco-entity-lockup__degree"])[{i}]').text
                    number_level = number_level[2:3]
                    number_level = int(number_level)

                    # Фильтр связи только для уровня  - 2
                    if number_level == 2:
                        # получаем текст статуса
                        amount_elements_1 = self.browser.find_element(By.XPATH, f'(//div[@class="artdeco-entity-lockup__caption ember-view"])[{i}]').text
                        amount_elements_1 = str(amount_elements_1).lower()

                        # Очищаем строку, оставляя только буквы
                        reg = re.compile('[^a-zA-Z а-яА-Я]')
                        reg = reg.sub('', amount_elements_1)
                        amount_elements_split = reg.split() # список слов из статуса

                        count_key = len(text_key) # количество ключей в списке
                        count_element = len(amount_elements_split) # количество слов в статусе пользователя


                        # Проверка равенства ключа и одного из слов, из статуса пользователя
                        status_search_start = True
                        for j in range(0, count_key):
                            for n in range(0, count_element):
                                if status_search_start:
                                    if text_key[j] == amount_elements_split[n]:
                                        status_search_start = False
                                        print(f'Уровень связи: {number_level}')
                                        print(f'Найден подходящий кандидат по ключу: << {text_key[j]} >>')

                                        # получаем ссылку на страницу пользователя
                                        atr = self.browser.find_element(By.XPATH,
                                                                        f'(//div[@class="inline-flex full-width"]//a[@tabindex="0"])[{i}]')
                                        # Выводим ссылку в консоль
                                        atr_check = atr.get_attribute('href')
                                        print(atr_check)


                                        first_window = self.browser.window_handles[0]  # получаем имя первого окна браузера

                                        # Создаем новую вкладку / открываем ссылку
                                        self.browser.execute_script(
                                            "window.open('about:blank', 'tab2');")  # Открывает новую пустую вкладку
                                        window_after = self.browser.window_handles[1]
                                        self.browser.switch_to.window(window_after)
                                        # Открываем полученную ссылку
                                        self.browser.get(atr_check)
                                        time.sleep(2)
                                        self.browser.switch_to.window('tab2')

                                        # Проверка элемента '+', что бы не нажать на отслеживание ленты.
                                        text_button_from_user = self.is_element_present(*HomePageLocators.ELEM_PLUS_BUTTON_FROM_USER)
                                        # Проверка элемента '\/', что бы не нажать кнопку, которая уже на РАССМОТРЕНИИ.
                                        text_button_from_user_2 = self.is_element_present(*HomePageLocators.ELEM_PLUS_BUTTON_FROM_USER_2)

                                        print(f'ОТСЛЕЖИВАТЬ: {text_button_from_user}')
                                        print(f'РАССМОТРЕНИЕ: {text_button_from_user}')

                                        if text_button_from_user is True or text_button_from_user_2 is True:
                                            time.sleep(3)
                                            self.browser.execute_script('window.close()')  # Закрыть текущую вкладку
                                            self.browser.switch_to.window(first_window)
                                            break

                                        else:
                                            if text_button_from_user is False or text_button_from_user_2 is False:
                                                time.sleep(3)
                                                self.browser.find_element(
                                                    *HomePageLocators.ELEM_BUTTON_SETUP_CONTACT).click()
                                                print('кнопка 1 << УСТАНОВИТЬ КОНТАКТ >> "ok"')

                                                time.sleep(3)
                                                self.browser.find_element(*HomePageLocators.SEND_REGUEST_BUTTON).click()
                                                print('кнопка 2 << ОТПРАВИТЬ ПРИГЛАШЕНИЕ >> "ok"')

                                                if self.is_element_present(*HomePageLocators.ELEM_PLUS_BUTTON_FROM_USER_2):
                                                    print('ПРИГЛАШЕНИЕ УСПЕШНО ОТПРАВЛЕНО\n')

                                                else:
                                                    print('Достигнуто максимальное количество добавлений')
                                                    script_stopped = True
                                                    break




                                                time.sleep(2)

                                                self.browser.execute_script('window.close()')  # Закрыть текущую вкладку
                                                self.browser.switch_to.window(first_window) # Переключаем на первую вкладку
                                                time.sleep(2)
                                                self.browser.find_element(*HomePageLocators.BUTTON_EXIT)

                                                break






















