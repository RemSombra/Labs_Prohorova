from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def test_case() -> None:
    driver = webdriver.Edge()
    driver.get('https://qa.neapro.site/login')

    driver.find_element(
        By.CSS_SELECTOR, '.fieldset:nth-child(1) input').click()
    driver.find_element(
        By.CSS_SELECTOR, '.fieldset:nth-child(1) input').send_keys('blackleprosy@gmail.com')
    driver.find_element(
        By.CSS_SELECTOR, '.fieldset:nth-child(2) input').click()
    driver.find_element(
        By.CSS_SELECTOR, '.fieldset:nth-child(2) input').send_keys('123456789')
    driver.find_element(By.CSS_SELECTOR, '.btn').click()

    print("Success")
    driver.close()


if __name__ == "__main__":
    print("Test case")
    test_case()
