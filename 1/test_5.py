from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException


def test_case(email : str, password : str) -> None:
    driver = webdriver.Edge()
    driver.find_element(
        By.XPATH, '//*[@id="admin_email"]').send_keys(email)
    driver.find_element(
        By.XPATH, '//*[@id="admin_password"]').send_keys(password)
    driver.find_element(
        By.XPATH, '//*[@id="admin_submit_action"]/input').click()

    try:
        driver.find_element(By.XPATH, '//*[@id="current_user"]')
        print("Success")
    except NoSuchElementException:
        print("Failed")

    driver.close()


if __name__ == "__main__":
    print("Test case 1")
    test_case("test_wrong_email@mail.ru", "test_wrong_password")

    print("test case 2")
    test_case("abc123@mail.ru", "abcABC123456")
