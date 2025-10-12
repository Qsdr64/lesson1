import pytest
from selenium import webdriver
from Pageshop import shoping

@pytest.fixture 
def driver():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()
def testshop(driver):
    shopping_page = shoping(driver)
    shopping_page.authorization()
    shopping_page.basket()
    shopping_page.price()
    shopping_page.shop()
