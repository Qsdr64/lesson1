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
checkout = WebDriverWait (driver, 3)
checkout.until(EC.url_to_be("https://www.saucedemo.com/cart.html"))
driver.find_element(By.CSS_SELECTOR, ("#checkout")).click()
swag = WebDriverWait (driver, 3)
swag.until(EC.url_to_be("https://www.saucedemo.com/checkout-step-one.html"))
driver.find_element(By.CSS_SELECTOR, ("#first-name")).send_keys("Valeriy")
driver.find_element(By.CSS_SELECTOR, ("#last-name")).send_keys("Nugmanov")
driver.find_element(By.CSS_SELECTOR, ("#postal-code")).send_keys("413276")
driver.find_element(By.CSS_SELECTOR,("#continue")).click()
prise = WebDriverWait(driver, 3)
prise.until(EC.url_to_be("https://www.saucedemo.com/checkout-step-two.html"))
total = driver.find_element(By.CLASS_NAME,("summary_total_label"))
assert total.text == "Total: $58.29"
driver.quit()
