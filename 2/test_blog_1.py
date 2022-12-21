from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test(successful_title : str) -> None:
    driver = webdriver.Edge()

    driver.get("https://блог.новео.рф")

    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "[type=search]").send_keys("валидация")

    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "[type=search]").send_keys(Keys.ENTER)

    sleep(1)
    driver.find_element(By.TAG_NAME, "article").click()

    sleep(1)
    title = driver.find_element(By.CSS_SELECTOR, "article>header>h2").text

    assert title == successful_title, "Test Failed"
    print("Complete")

    sleep(1)
    driver.close()

if __name__ == "__main__":
    print("test case 1")
    test("Валидация данных в Nest")

    print("test case 2 wrong")
    test("Wrong title")