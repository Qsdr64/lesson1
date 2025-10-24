import pytest
from selenium import webdriver
from PageObject import Calcul
import allure

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()

def testcalc(driver):
    calculator = Calcul(driver)
    with allure.step("Начинаем тест калькулятора"):
        calculator.clickcalc()
        calculator.examination()
