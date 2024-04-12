from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

link = 'https://suninjuly.github.io/file_input.html'

file = os.path.abspath(os.path.dirname(__file__)) + '\\file.txt'

browser = webdriver.Chrome()
browser.get(link)

try:

    browser.find_element(By.NAME, 'firstname').send_keys('Petya')

    browser.find_element(By.NAME, 'lastname').send_keys('Petrov')

    browser.find_element(By.NAME, 'email').send_keys('Petya@Petrov.petrovich')

    browser.find_element(By.ID, 'file').send_keys(file)

    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

finally:
    sleep(5)
    browser.quit()