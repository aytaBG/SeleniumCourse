from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()

#"alert(' ')";  -  всплывающее окно
browser.execute_script("alert('Robots at work');")

sleep(5)

#"document.title=' '";  -  название страницы
browser.execute_script("document.title='Script executing';")

#"return arguments[0].scrollIntoView(true);" элемент,  -  проскролить страницу до видимости элемента
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)

#"window.scrollBy(x, y);" проскролить страницу на x пикселей вправо и y вниз
browser.execute_script("window.scrollBy(0, 0);")

sleep(5)

browser.quit()

