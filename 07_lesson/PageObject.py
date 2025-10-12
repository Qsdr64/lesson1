from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

class Calcul:
    
    def __init__(self, driver):
        self.driver = driver
    def clickcalc (self):
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")
        self.driver.find_element(By.XPATH,f"//span[text()='{7}']").click()
        self.driver.find_element(By.XPATH,f"//span[text()='+']").click()
        self.driver.find_element(By.XPATH,f"//span[text()='{8}']").click()
        self.driver.find_element(By.XPATH,f"//span[text()='=']").click()
    def examination(self):
        wait = WebDriverWait(self.driver, 45)
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
    )
        result_locator = self.driver.find_element(By.CSS_SELECTOR, "div.screen")
        assert result_locator.text == "15"