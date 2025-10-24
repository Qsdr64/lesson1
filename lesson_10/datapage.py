from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
@allure.title("Тест калькулятора")
@allure.description("Проверка работы калькулятора на сайте")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
class data:
    def __init__(self, driver)-> None:
        """Инициализация класса с драйвером браузера."""
        self.driver = driver
    def data (self)-> None:
        """
        Метод ожидает загрузки страницы корзины, затем кликает по кнопке оформления заказа.
        """
        checkout = WebDriverWait (self.driver, 3)
        checkout.until(EC.url_to_be("https://www.saucedemo.com/cart.html"))
        self.driver.find_element(By.CSS_SELECTOR, ("#checkout")).click()