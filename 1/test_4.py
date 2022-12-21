from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def test_case() -> None:
    driver = webdriver.Edge()
    driver.get('https://adminqa.neapro.site/login')

    driver.find_element(
        By.XPATH, '//*[@id="admin_email"]').send_keys('moderat@neapro.ru')
    driver.find_element(
        By.XPATH, '//*[@id="admin_password"]').send_keys('Aa123456')
    driver.find_element(
        By.XPATH, '//*[@id="admin_submit_action"]/input').click()

    print("Success")
    driver.close()


if __name__ == "__main__":
    print("Test case")
    test_case()
