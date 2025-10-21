from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService())

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

delay = driver.find_element(By.CSS_SELECTOR, "#delay")
delay.clear()
delay.send_keys("45")

driver.find_element(By.XPATH,f"//span[text()='{7}']").click()
driver.find_element(By.XPATH,f"//span[text()='+']").click()
driver.find_element(By.XPATH,f"//span[text()='{8}']").click()
driver.find_element(By.XPATH,f"//span[text()='=']").click()

wait = WebDriverWait(driver, 45)
result_locator = (By.CSS_SELECTOR, "#screen")
assert wait.until(EC.text_to_be_present_in_element(result_locator, "15"))
