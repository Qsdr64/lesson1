from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
@allure.title("Оформление заказа")
@allure.feature("Оформление")
@allure.severity(allure.severity_level.CRITICAL)
class shoping:
    def __init__(self, driver)-> None:
        """Инициализация класса с драйвером браузера."""
        self.driver = driver
    def basket (self)-> None:
        """
        Ожидает загрузки страницы с URL 'https://www.saucedemo.com/checkout-step-one.html',
        затем заполняет поля для имени, фамилии и почтового индекса в форме,
        и переходит к следующему шагу оформления заказа, кликая по кнопке "Continue".
        """
        swag = WebDriverWait (self.driver, 3)
        swag.until(EC.url_to_be("https://www.saucedemo.com/checkout-step-one.html"))
        self.driver.find_element(By.CSS_SELECTOR, ("#first-name")).send_keys("Valeriy")
        self.driver.find_element(By.CSS_SELECTOR, ("#last-name")).send_keys("Nugmanov")
        self.driver.find_element(By.CSS_SELECTOR, ("#postal-code")).send_keys("413276")
        self.driver.find_element(By.CSS_SELECTOR,("#continue")).click()
