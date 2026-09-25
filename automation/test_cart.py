
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_add_product_to_cart():

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

        # Add Laptop to cart
        add_to_cart_buttons = driver.find_elements(By.XPATH, "//button[text()='Add to Cart']")
        add_to_cart_buttons[0].click()

        # Open cart
        driver.find_element(By.XPATH, "//button[text()='View Cart']").click()

        # Verify cart page
        assert "Shopping Cart" in driver.title

        # Verify Laptop is in cart
        assert "Laptop" in driver.page_source

        # Verify Laptop price
        assert "₹55000" in driver.page_source

    finally:
        driver.quit()
