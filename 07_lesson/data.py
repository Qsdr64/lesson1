from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class data:
    def __init__(self, driver):
        self.driver = driver
    def data (self):
        checkout = WebDriverWait (self.driver, 3)
        checkout.until(EC.url_to_be("https://www.saucedemo.com/cart.html"))
        self.driver.find_element(By.CSS_SELECTOR, ("#checkout")).click()