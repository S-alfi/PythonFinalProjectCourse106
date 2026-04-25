

# Playwright assignments:

# Date: 22.03.2026
# Assignment - 02

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://demoqa.com/login")

    new_user = page.locator('#newUser')
    new_user.click()

    first_name = page.locator('#firstname')
    first_name.click()
    first_name.clear()
    first_name.fill("Dixon")

    last_name = page.locator('#lastname')
    last_name.click()
    last_name.clear()
    last_name.fill("Sider")

    user_name = page.locator('#userName')
    user_name.click()
    user_name.clear()
    user_name.fill("new_user_01")

    password = page.locator('#password')
    password.click()
    password.fill("new_password_01")

    register = page.locator('#register')
    register.click()

    back_to_login_button = page.locator('#gotologin')
    back_to_login_button.click()

    user_name = page.locator('#userName')
    user_name.click()
    user_name.fill("new_user_01")

    password = page.locator('#password')
    password.click()
    password.fill("new_password_01")

    login_button = page.locator('#login')
    login_button.click()

    browser.close()

