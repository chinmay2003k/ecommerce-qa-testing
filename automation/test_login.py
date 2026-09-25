from selenium import webdriver
from selenium.webdriver.common.by import By


def test_valid_login():

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("http://127.0.0.1:5000/login")

        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "password").send_keys("Test@123")

        driver.find_element(By.ID, "login-button").click()

        assert "Products" in driver.title

    finally:
        driver.quit()