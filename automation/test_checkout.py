from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def test_checkout_order():

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)

    try:
        # Open Login Page
        driver.get("http://127.0.0.1:5000/login")

        # Login
        wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys("testuser")

        driver.find_element(
            By.ID, "password"
        ).send_keys("Test@123")

        driver.find_element(
            By.ID, "login-button"
        ).click()

        # Wait for Products Page
        wait.until(EC.title_contains("Products"))

        # Find Add to Cart buttons
        add_to_cart_buttons = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//button[text()='Add to Cart']")
            )
        )

        # Add first product to cart
        add_to_cart_buttons[0].click()

        # Open Cart
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[@href='/cart']")
            )
        ).click()

        # Wait for Cart Page
        wait.until(EC.url_contains("/cart"))

        # Verify cart contains product
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Laptop')]")
            )
        )

        # Open Checkout directly
        driver.get("http://127.0.0.1:5000/checkout")

        # Wait for Checkout Page
        wait.until(EC.url_contains("/checkout"))

        # Enter Customer Name
        wait.until(
            EC.presence_of_element_located(
                (By.ID, "name")
            )
        ).send_keys("Test User")

        # Enter Address
        driver.find_element(
            By.ID, "address"
        ).send_keys("Mumbai")

        # Select Payment Method
        payment = Select(
            wait.until(
                EC.presence_of_element_located(
                    (By.ID, "payment")
                )
            )
        )

        payment.select_by_value("upi")

        # Click Place Order
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "place-order")
            )
        ).click()

        # Wait for successful order message
        wait.until(
            lambda d: "Order placed successfully!" in d.page_source
        )

        # Verify successful order
        assert "Order placed successfully!" in driver.page_source

    finally:
        driver.quit()