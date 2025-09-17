from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService())
skypro = WebDriverWait(driver, 20)
driver.get("http://uitestingplayground.com/textinput")
newname = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
newname.send_keys("Skypro")
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
skypro.until(EC.text_to_be_present_in_element(
    (By.CSS_SELECTOR, "#updatingButton"), "Skypro"))
button_text = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(button_text)
driver.quit()
