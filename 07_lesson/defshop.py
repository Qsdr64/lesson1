from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class shop:
    def __init__(self, driver):
        self.driver = driver
    def shop (self):
        Sale = WebDriverWait (self.driver, 3)
        Sale.until(EC.url_to_be('https://www.saucedemo.com/inventory.html'))
        self.driver.find_element(
             By.CSS_SELECTOR, ("#add-to-cart-sauce-labs-backpack")).click()
        self.driver.find_element(
            By.CSS_SELECTOR, ("#add-to-cart-sauce-labs-bolt-t-shirt")).click()
        self.driver.find_element(
            By.CSS_SELECTOR, ("#add-to-cart-sauce-labs-onesie")).click()
        self.driver.find_element(By.CLASS_NAME, ("shopping_cart_link")).click()