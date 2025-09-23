from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.implicitly_wait(20)
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

name = driver.find_element(By.NAME, ("first-name")).send_keys("Иван")
Last_name = driver.find_element(By.NAME, ("last-name")).send_keys("Петров")
Address = driver.find_element(By.NAME, ("address")).send_keys("Ленина, 55-3")
Zip = driver.find_element(By.NAME, ("zip-code")).send_keys("")
City = driver.find_element(By.NAME, ("city")).send_keys("Москва")
Country = driver.find_element(By.NAME, ("country")).send_keys("Россия")
Email = driver.find_element(By.NAME, ("e-mail")).send_keys("test@skypro.com")
Phone_number = driver.find_element(By.NAME, ("phone")).send_keys("+7985899998787")
Job_position = driver.find_element(By.NAME, ("job-position")).send_keys("QA")
company = driver.find_element(By.NAME, ("company")).send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

zip_field = driver.find_element(By.NAME, "zip-code")
zip_color = zip_field.value_of_css_property("background-color")
assert zip_color == "rgb(255, 0, 0)", "Zip code не подсвечен красным"

all_fields = driver.find_elements(By.TAG_NAME, "input")

for field in all_fields:
    if field.get_attribute("name") != "zip-code":
        color = field.value_of_css_property("background-color")
        assert color == "rgb(0, 128, 0)", f"Поле {field.get_attribute('name')} не подсвечено зелёным"

driver.quit()