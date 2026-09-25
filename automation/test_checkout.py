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
        driver.get("http://127.0.0.1:5000/login")

        wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys("testuser")

        driver.find_element(By.ID, "password").send_keys("Test@123")
        driver.find_element(By.ID, "login-button").click()

        wait.until(EC.title_contains("Products"))

        add_to_cart_buttons = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//button[text()='Add to Cart']")
            )
        )

        add_to_cart_buttons[0].click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[@href='/cart']")
            )
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[@href='/checkout']")
            )
        ).click()

        wait.until(EC.title_contains("Checkout"))

        wait.until(
            EC.presence_of_element_located((By.ID, "name"))
        ).send_keys("Test User")

        driver.find_element(
            By.ID, "address"
        ).send_keys("Mumbai")

        Select(
            driver.find_element(By.ID, "payment")
        ).select_by_value("upi")

        driver.find_element(By.ID, "place-order").click()

        wait.until(
            lambda d: "Order placed successfully!" in d.page_source
        )

        assert "Order placed successfully!" in driver.page_source

    finally:
        driver.quit()