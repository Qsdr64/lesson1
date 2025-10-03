from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class price:
    def __init__(self, driver):
        self.driver = driver
    def price(self):
        prise = WebDriverWait(self.driver, 3)
        prise.until(EC.url_to_be("https://www.saucedemo.com/checkout-step-two.html"))
        total = self.driver.find_element(By.CLASS_NAME,("summary_total_label"))
        assert total.text == "Total: $58.29"