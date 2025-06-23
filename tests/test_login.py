# test_login.py
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_success():
    # Set up WebDriver
    options = Options()
    # options.add_argument("--headless")  # Remove this if you want to see browser
    driver = webdriver.Chrome(service=ChromeService(), options=options)
    driver.maximize_window()
    driver.get("https://practicetestautomation.com/practice-test-login/")

        # Step 2: Find username field and enter text
    username = driver.find_element(By.ID, "username")
    username.send_keys("student")

        # Step 3: Find password field and enter text
    password = driver.find_element(By.ID, "password")
    password.send_keys("Password123")

        # Step 4: Click the submit button
    submit_btn = driver.find_element(By.ID, "submit")
    submit_btn.click()

        # Step 5: Wait for new page and verify success
    WebDriverWait(driver, 10).until(EC.url_contains("logged-in-successfully"))
    assert "Congratulations" in driver.page_source
    print("✅ Login test passed!")


