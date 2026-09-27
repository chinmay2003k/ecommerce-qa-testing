from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_products_page():

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)

    try:
        # Open login page
        driver.get("http://127.0.0.1:5000/login")

        # Login
        wait.until(
            EC.presence_of_element_located(
                (By.ID, "username")
            )
        ).send_keys("testuser")

        driver.find_element(
            By.ID, "password"
        ).send_keys("Test@123")

        driver.find_element(
            By.ID, "login-button"
        ).click()

        # Wait for Products page
        wait.until(
            EC.title_contains("Products")
        )

        # Verify products page
        assert "Products" in driver.title

        # Verify products are displayed
        products = wait.until(
            EC.presence_of_all_elements_located(
                (By.TAG_NAME, "h3")
            )
        )

        assert len(products) == 4

        # Verify product names
        product_names = [product.text for product in products]

        assert "Laptop" in product_names
        assert "Wireless Mouse" in product_names
        assert "Keyboard" in product_names
        assert "Headphones" in product_names

    finally:
        driver.quit()