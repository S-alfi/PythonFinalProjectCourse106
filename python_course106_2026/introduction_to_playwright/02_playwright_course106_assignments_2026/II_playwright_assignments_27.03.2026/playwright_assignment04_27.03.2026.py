

# Playwright assignments:

# Date: 27.03.2026
# Assignment - 04

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")

    login_info = page.query_selector_all('[class="input_error form_input"]')

    user_name = login_info[0]
    user_name.click()
    user_name.fill("standard_user")

    password = login_info[1]
    password.click()
    password.fill("secret_sauce")

    login_button = page.locator('[name="login-button"]')
    login_button.click()

    browser.close()

