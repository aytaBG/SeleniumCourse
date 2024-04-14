from selenium.webdriver.common.by import By
import pytest

class TestRework:

    @pytest.mark.smoke
    def test_1(self, browser):

        browser.get('https://suninjuly.github.io/registration1.html')

        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
        input3.send_keys("Smolensk")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        assert welcome_text == "Congratulations! You have successfully registered!"

    @pytest.mark.smoke
    def test_2(self, browser):

        browser.get('https://suninjuly.github.io/registration2.html')

        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
        input3.send_keys("Smolensk")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        assert welcome_text == "Congratulations! You have successfully registered!"

if __name__ == '__main__':
    pytest.main()

