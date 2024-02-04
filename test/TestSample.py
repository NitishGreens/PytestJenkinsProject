import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By


class TestEmployee:
    @pytest.fixture()
    def setup(self):
        options = ChromeOptions()
        options.add_experimental_option(name="detach", value=True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(url="https://adactinhotelapp.com/")
        yield
        self.driver.quit()

    def test_login(self,setup):
        txt_username = self.driver.find_element(By.ID, "username")
        txt_username.send_keys("bala@gmail.com")

        txt_password = self.driver.find_element(By.ID, "password")
        txt_password.send_keys("bala@123")

        btn_login = self.driver.find_element(By.NAME, "login")
        btn_login.click()
