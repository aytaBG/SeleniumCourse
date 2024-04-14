import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# получить email + пароль из файла
@pytest.fixture(scope='class')
def login():
    epass = ['', '']
    with open('login.txt') as logininf:
        epass[0] = logininf.readline().strip()
        epass[1] = logininf.readline().strip()
        return epass

@pytest.mark.t365
class Tests:

    @pytest.mark.parametrize('url', ['895', '896', '897', '898', '899', '903', '904', '905'])
    def testvaration(self, url, browser, login):
        #зайти на сайт
        link = f'https://stepik.org/lesson/236{url}/step/1'
        browser.get(link)

        #залогиниться
        browser.find_element(By.CLASS_NAME, 'navbar__auth_login').click()
        browser.find_element(By.ID, 'id_login_email').send_keys(login[0])
        browser.find_element(By.ID, 'id_login_password').send_keys(login[1])
        browser.find_element(By.CLASS_NAME, 'sign-form__btn.button_with-loader').click()
        WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located(
            (By.CLASS_NAME, 'learn-last-activity-dropdown__counter')))

        #ввести ответ
        browser.find_element(By.CLASS_NAME, 'ember-text-area').send_keys(str(math.log(int(time.time()))))
        browser.find_element(By.CLASS_NAME, 'submit-submission').click()

        #проверить ответ на соответствие
        answer = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
        assert answer == 'Correct!', print(answer)












