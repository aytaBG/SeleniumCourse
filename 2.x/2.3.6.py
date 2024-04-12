from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'https://suninjuly.github.io/redirect_accept.html'

browser = webdriver.Chrome()
browser.get(link)

try:

    browser.find_element(By.CLASS_NAME, 'trollface.btn.btn-primary').click()

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)

    browser.find_element(By.ID, 'answer').send_keys(y)

    browser.find_element(By.CSS_SELECTOR, '[type="submit"').click()

finally:
    sleep(5)
    browser.quit()