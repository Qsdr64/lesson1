from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")
    
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")
    
username_input.send_keys("tomsmith")
password_input.send_keys("SuperSecretPassword!")
    

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()
sleep(2)
flash_element = driver.find_element(By.CSS_SELECTOR, "div.flash.success")
print(flash_element.text.strip())
driver.quit()

