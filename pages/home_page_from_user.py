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



print('Напишите через пробел ключи поиска: >  ', end='')
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
            # скролинг вниз
            for i in range(1, 3):
                try:
                    self.browser.find_element(*HomePageLocators.BUTON_MORE_POSTS).click()
                    time.sleep(1)
                except BaseException:
                    break

            # возвращаемся к первому посту
            c = self.browser.find_elements(By.XPATH, f'//span[@class="feed-shared-actor__title"]')
            self.browser.execute_script("return arguments[0].scrollIntoView();", c[0])
            time.sleep(5)

            # Подсчет количества целевых элементов
            count_posts = int(
                len(self.browser.find_elements(By.XPATH, f'(//img[@data-test-reactions-icon-type="LIKE"])')))
            print(f"Найдено << {count_posts} >> постов")

            for x in range(1, count_posts + 1):
                if self.is_element_present(By.XPATH, f'(//img[@data-test-reactions-icon-type="LIKE"])[{x}]'):
                    elem_posts = WebDriverWait(self.browser, 50).until(EC.element_to_be_clickable((By.XPATH, f'(//img[@data-test-reactions-icon-type="LIKE"])[{x}]')))
                    elem_posts.click()
                    print(f'В работе пост №{x}')

                # проверяем что окно открылось
                window_like_ok = self.is_element_present(*HomePageLocators.WINDOW_LIKE_OK)
                assert window_like_ok is True, 'Окно со списком лайкнувших, не найдено'


                # Модуль прокрутки окна с юзерами. Нажатие кнопки в конце списка по ключу "count"
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
                                print(f'Статус клика << показать боьше контактов >>: {count}')
                            except BaseException:
                                count = False
                                print(f'Статус клика << показать боьше контактов >>: {count}')


                href_list = []*10**10 # список найденных ссылок на профили юзеров
                # Получаем количество лайкнувших в списке
                self.messege_positive_check('работа со списком юзеров')
                print()
                time.sleep(3)
                amount_elements = int(len(self.browser.find_elements(*HomePageLocators.STATUS_USER)))
                for i in range(1, amount_elements + 1):
                    # Выполнить если окно лайков обнаруженно.
                    if window_like_ok:
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
                                            atr = self.browser.find_element(By.XPATH, f'(//div[@class="inline-flex full-width"]//a[@tabindex="0"])[{i}]')

                                            atr_check = atr.get_attribute('href')
                                            # Выводим ссылку в консоль
                                            print(f'Добавляем в общий список: {atr_check}\n')
                                            # Добавляем ссылку в список
                                            href_list.append(atr_check)
                    else:
                        break


                print(f'количество подходящих юзеров: {len(href_list)}')
                time.sleep(2)
                first_window = self.browser.window_handles[0]  # получаем имя первого окна браузера
                # пока список с сылками полон, выполнять цикл
                while len(href_list) != 0:
                    for l in range(1, len(href_list) + 1):
                        # Создаем новую вкладку / открываем ссылку
                        self.browser.execute_script(
                            "window.open('about:blank', 'tab2');")  # Открывает новую пустую вкладку
                        window_after = self.browser.window_handles[1]
                        self.browser.switch_to.window(window_after)
                        # Открываем полученную ссылку
                        self.browser.get(href_list[l])

                        time.sleep(2)
                        self.browser.switch_to.window('tab2')

                        # РАБОТА С НОВЫМ ОКНОМ БРАУЗЕРА
                        # Проверка элемента '+', что бы не нажать на отслеживание ленты.
                        text_button_from_user = self.is_element_present(
                            *HomePageLocators.ELEM_PLUS_BUTTON_FROM_USER)
                        # Проверка элемента '\/', что бы не нажать кнопку, которая уже на РАССМОТРЕНИИ.
                        text_button_from_user_2 = self.is_element_present(
                            *HomePageLocators.ELEM_PLUS_BUTTON_FROM_USER_2)

                        print(f'ОТСЛЕЖИВАТЬ: {text_button_from_user}')
                        print(f'НА РАССМОТРЕНИИ: {text_button_from_user_2}')

                        # Если один из элементов True: - закрываем текущую вкладку и переходим обратно на первую.
                        if text_button_from_user is True or text_button_from_user_2 is True:
                            print('__не подходит, пропускаем__\n')
                            time.sleep(3)
                            self.browser.execute_script('window.close()')  # Закрыть текущую вкладку
                            self.browser.switch_to.window(first_window)
                            break

                        # Если все элементы Folse: - устанавливаем контакт и закрываем вкладку с переходом на первую.
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
                                    self.browser.execute_script('window.close()')  # Закрыть текущую вкладку
                                    self.browser.switch_to.window(first_window)  # Переключаем на первую вкладку

                                else:
                                    print('Достигнуто максимальное количество добавлений')
                                    print('РАБОТА ЗАВЕРШИНА УСПЕШНО')
                                    script_stopped = True
                                    break


            if window_like_ok:
                time.sleep(3)
                self.browser.find_element(*HomePageLocators.BUTTON_EXIT).click()
                if x == count_posts:
                    script_stopped = True
                    print('РАБОТА ЗАВЕРШИНА УСПЕШНО')
                    time.sleep(3)



































