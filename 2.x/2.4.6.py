from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/cats.html')

browser.find_element(By.ID, "button")