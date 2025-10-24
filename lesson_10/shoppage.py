from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
@allure.title("Заполнение корзины")
@allure.feature("Корзина")
@allure.severity(allure.severity_level.CRITICAL)
class shop:
    def __init__(self, driver)-> None:
        self.driver = driver
    def shop (self)-> None:
        """
        Выполняет действия на странице магазина:
        - ожидает загрузки страницы с URL 'https://www.saucedemo.com/inventory.html'
        - добавляет товары в корзину
        - переходит в корзину
        """
        Sale = WebDriverWait (self.driver, 3)
        Sale.until(EC.url_to_be('https://www.saucedemo.com/inventory.html'))
        self.driver.find_element(
             By.CSS_SELECTOR, ("#add-to-cart-sauce-labs-backpack")).click()
        self.driver.find_element(
            By.CSS_SELECTOR, ("#add-to-cart-sauce-labs-bolt-t-shirt")).click()
        self.driver.find_element(
            By.CSS_SELECTOR, ("#add-to-cart-sauce-labs-onesie")).click()
        self.driver.find_element(By.CLASS_NAME, ("shopping_cart_link")).click()