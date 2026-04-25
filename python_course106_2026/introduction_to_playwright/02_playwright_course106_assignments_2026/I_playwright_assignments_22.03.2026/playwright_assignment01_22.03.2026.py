

# Playwright assignments:

# Date: 22.03.2026
# Assignment - 01

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://demo.applitools.com/#")

    user_name = page.locator('#username')
    user_name.click()
    user_name.clear()
    user_name.fill("new_user_01")

    password = page.locator('#password')
    password.click()
    password.fill("new_password_01")

    sign_in_button = page.locator('#log-in')
    sign_in_button.click()

    browser.close()

