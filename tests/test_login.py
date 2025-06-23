import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_success():
    options = Options()
    # options.add_argument("--headless")  # comment this to see browser
    driver = webdriver.Chrome(service=ChromeService(), options=options)
    driver.maximize_window()

    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()

        WebDriverWait(driver, 10).until(EC.url_contains("logged-in-successfully"))
        assert "Congratulations" in driver.page_source

    finally:
        driver.quit()
