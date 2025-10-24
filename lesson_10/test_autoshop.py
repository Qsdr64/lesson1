from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from selenium import webdriver
from Pageauthorization import authorization
from shoppage import shop
from datapage import data
from Pagdata import shoping
from Pageprice import price
import allure

@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    yield driver
    driver.quit()

def testing(browser):
    with allure.step("Авторизация пользователя"):
        avtoriz = authorization(browser)
        avtoriz.open()
        avtoriz.authorization()

    with allure.step("Переход в магазин и выбор товара"):
        pokupka = shop(browser)
        pokupka.shop()

    with allure.step("Просмотр данных товара"):
        page_data = data(browser)
        page_data.data()

    with allure.step("Добавление товара в корзину"):
        page_shop = shoping(browser)
        page_shop.basket()

    with allure.step("Проверка цены товара"):
        page_price = price(browser)
        page_price.price()