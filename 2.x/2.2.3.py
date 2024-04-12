from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link = 'https://suninjuly.github.io/selects2.html'

browser = webdriver.Chrome()
browser.get(link)

try:

    x = int(browser.find_element(By.ID, 'num1').text) + int(browser.find_element(By.ID, 'num2').text)

    #sleep(10)

    browser.find_element(By.ID, 'dropdown').click()

    #sleep(10)
    dest = '//select/*[contains(text(), "' + str(x) + '")]'

    browser.find_element(By.XPATH, dest).click()

    #sleep(10)

    browser.find_element(By.CLASS_NAME, 'btn.btn-default').click()

finally:
    sleep(5)
    browser.quit()