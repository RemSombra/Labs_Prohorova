import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestAuthandlogout2():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_authandlogout2(self):
        self.driver.get("https://do.rsue.ru")
        self.driver.find_element(
            By.NAME, "username").send_keys("vorotintcevav")
        self.driver.find_element(By.NAME, "password").send_keys("7xq4otaweb9k")
        self.driver.find_element(By.ID, "loginbtn").click()
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Выход").click()
