import pytest
from selenium import webdriver
from PageObject import Calcul

@pytest.fixture 
def driver ():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()
def testcalc(driver):
    calculator = Calcul(driver)
    calculator.clickcalc()
    calculator.examination()
