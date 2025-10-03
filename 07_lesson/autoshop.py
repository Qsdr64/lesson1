from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from authorization import authorization
from defshop import shop
from data import data
from Pageshop import shoping
from price import price
@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    yield driver 
    driver.quit()
def testing(browser):
    avtoriz = authorization(browser)
    avtoriz.open()
    avtoriz.authorization()

    pokupka = shop(browser)
    pokupka.shop()

    page_data = data(browser)
    page_data.data()

    page_shop = shoping(browser)
    page_shop.basket()

    page_price = price(browser)
    page_price.price()