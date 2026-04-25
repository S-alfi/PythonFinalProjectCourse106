

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")

    user_name = page.locator('[name="user-name"]')
    user_name.click()
    user_name.clear()
    user_name.fill("standard_user")

    password = page.locator('[name="password"]')
    password.click()
    password.clear()
    password.fill("secret_sauce")

    login_button = page.locator('[name="login-button"]')
    login_button.click()

    browser.close()

