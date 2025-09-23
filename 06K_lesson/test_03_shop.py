from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
    )
driver.get("https://www.saucedemo.com/")
user = driver.find_element(By.CSS_SELECTOR, ('#user-name') )
user.send_keys("standard_user")
password = driver.find_element(By.CSS_SELECTOR, ("#password"))
password.send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, ("#login-button")).click()
Sale = WebDriverWait (driver, 3)
Sale.until(EC.url_to_be('https://www.saucedemo.com/inventory.html'))
driver.find_element(
    By.CSS_SELECTOR, ("#add-to-cart-sauce-labs-backpack")).click()

driver.find_element(
    By.CSS_SELECTOR, ("#add-to-cart-sauce-labs-bolt-t-shirt")).click()

driver.find_element(
    By.CSS_SELECTOR, ("#add-to-cart-sauce-labs-onesie")).click()
driver.find_element(By.CLASS_NAME, ("shopping_cart_link")).click()
Checkout = WebDriverWait (driver, 3)
Checkout.until(EC.url_to_be("https://www.saucedemo.com/cart.html"))
driver.find_element(By.CSS_SELECTOR, ("#checkout")).click()
Swag = WebDriverWait (driver, 3)
Swag.until(EC.url_to_be("https://www.saucedemo.com/checkout-step-one.html"))
First = driver.find_element(By.CSS_SELECTOR, ("#first-name"))
First.send_keys("Valeriy")
Last = driver.find_element(By.CSS_SELECTOR, ("#last-name"))
Last.send_keys("Nugmanov")
code = driver.find_element(By.CSS_SELECTOR, ("#postal-code"))
code.send_keys("413276")
driver.find_element(By.CSS_SELECTOR,("#continue")).click()
Prise = WebDriverWait(driver, 3)
Prise.until(EC.url_to_be("https://www.saucedemo.com/checkout-step-two.html"))
Total = driver.find_element(By.CLASS_NAME,("summary_total_label"))
if Total == "$58.29":
    print ("Итоговая ценна равна $58.29")
else:
    print ("Итоговая ценнв не равна $58.29")
