from selenium.webdriver.common.by import By
import allure
@allure.title("Авторизация на сайте")
@allure.description("Проверка авторизации")
@allure.feature("Авторизация")
@allure.severity(allure.severity_level.CRITICAL)
class authorization:
    url = "https://www.saucedemo.com/"
    def __init__(self, driver)-> None:
        """Инициализация класса с драйвером браузера."""
        self.driver = driver
    def open(self)-> None:
        """
        Открывает страницу авторизации по заданному URL.
        """
        self.driver.get(self.url)
    def authorization (self)-> None:
        """
        Производит вход в систему, заполняя поля для имени пользователя и пароля, 
        а затем кликает кнопку входа.
        """
        self.driver.find_element(By.CSS_SELECTOR, ('#user-name') ).send_keys("standard_user")     
        self.driver.find_element(By.CSS_SELECTOR, ("#password")).send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, ("#login-button")).click()