import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'https://suninjuly.github.io/math.html'

browser = webdriver.Chrome()
browser.get(link)

try:

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    textbox = browser.find_element(By.ID, 'answer')
    textbox.send_keys(y)

    browser.find_element(By.ID, 'robotCheckbox').click()

    browser.find_element(By.ID, 'robotsRule').click()

    browser.find_element(By.CLASS_NAME, 'btn.btn-default').click()

finally:
    sleep(5)
    browser.quit()
