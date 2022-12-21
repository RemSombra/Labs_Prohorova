from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_case(slug : str, successful_title : str) -> None:

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)

    driver.get(f"https://блог.новео.рф/{slug}")

    sleep(1)
    title = driver.find_element(By.CSS_SELECTOR, "article>header>h2").text
    assert title == successful_title, "Test Failed"
    print("Complete")

    sleep(1)
    driver.close()


if __name__ == "__main__":
    print("test case 1")
    test_case("2022/10/validatsiya-dannyh-v-nest/",
              "Валидация данных в Nest")

    print("test case 2")
    test_case("2022/09/timbilding-ekstrima-i-prikljuchenij/",
              "Тимбилдинг экстрима и приключений!")

    print("test case 3")
    test_case("2022/09/timbilding-ekstrima-i-prikljuchenij/",
              "Тимбилдинг приключений и экстрима?")
