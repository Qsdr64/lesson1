from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class shoping:
    def __init__(self, driver):
        self.driver = driver
    def basket (self):
        swag = WebDriverWait (self.driver, 3)
        swag.until(EC.url_to_be("https://www.saucedemo.com/checkout-step-one.html"))
        self.driver.find_element(By.CSS_SELECTOR, ("#first-name")).send_keys("Valeriy")
        self.driver.find_element(By.CSS_SELECTOR, ("#last-name")).send_keys("Nugmanov")
        self.driver.find_element(By.CSS_SELECTOR, ("#postal-code")).send_keys("413276")
        self.driver.find_element(By.CSS_SELECTOR,("#continue")).click()
