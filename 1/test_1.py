from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def test_case() -> None:
    driver = webdriver.Edge()
    driver.get('https://adminqa.neapro.site/login')

    driver.find_element(By.ID, 'admin_email').click()
    driver.find_element(By.ID, 'admin_email').send_keys('abc123@neapro.ru')
    driver.find_element(By.ID, 'admin_password').click()
    driver.find_element(By.ID, 'admin_password').send_keys('abcABC123456')
    driver.find_element(By.NAME, 'commit').click()

    print("Success")
    driver.close()


if __name__ == "__main__":
    print("Test case")
    test_case()
