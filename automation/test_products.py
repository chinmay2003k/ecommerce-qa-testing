
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_products_page():

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        # Open login page
        driver.get("http://127.0.0.1:5000/login")

        # Login
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "password").send_keys("Test@123")
        driver.find_element(By.ID, "login-button").click()

        # Verify products page
        assert "Products" in driver.title

        # Verify products are displayed
        products = driver.find_elements(By.TAG_NAME, "h3")

        assert len(products) == 4

        # Verify product names
        product_names = [product.text for product in products]

        assert "Laptop" in product_names
        assert "Wireless Mouse" in product_names
        assert "Keyboard" in product_names
        assert "Headphones" in product_names

    finally:
        driver.quit()
