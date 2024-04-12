from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

email = ''
password = ''

link = 'https://suninjuly.github.io/alert_accept.html'

browser = webdriver.Chrome()
browser.implicitly_wait(15)
browser.get(link)

try:

    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

    browser.switch_to.alert.accept()

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)

    browser.find_element(By.ID, 'answer').send_keys(y)

    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

    #скопировать ответ из алёрта
    alert_text = browser.switch_to.alert.text.split(': ')[-1]
    browser.switch_to.alert.accept()

    #перейти на степик
    browser.get('https://stepik.org/learn')

    #залогиниться
    browser.find_element(By.ID, 'id_login_email').send_keys(email)
    browser.find_element(By.ID, 'id_login_password').send_keys(password)
    browser.find_element(By.CLASS_NAME, 'sign-form__btn.button_with-loader').click()

    #зайти на текущий урок
    browser.find_element(By.CLASS_NAME, 'lfcc__continue-btn').click()

    #вставить ответ, подтвердить, дождаться проверки и перейти на следующий урок
    browser.find_element(By.CLASS_NAME, 'ember-text-area.ember-view.textarea.string-quiz__textarea').send_keys(alert_text)
    browser.find_element(By.CLASS_NAME, 'submit-submission').click()
    WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'attempt-message_correct')))
    browser.find_element(By.CLASS_NAME, 'lesson__next-btn').click()

finally:

    browser.quit()