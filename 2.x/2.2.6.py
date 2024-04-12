from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from time import sleep

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'https://suninjuly.github.io/execute_script.html'

browser = webdriver.Chrome()
browser.get(link)

try:

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)

    textbox = browser.find_element(By.ID, 'answer')
    textbox.send_keys(y)
    textbox.click()

    browser.find_element(By.ID, 'robotCheckbox').click()

    radio = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

finally:
    sleep(5)
    browser.quit()