

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

    # A drop-down menu is a graphical user interface (GUI) element that allows a user to choose one option from a list.

    drop_down_menu = page.locator('[class="product_sort_container"]')

    # The first method to select a value from a drop-down menu using its index.

    drop_down_menu.select_option(index=2)

    # The second method to select a value from a drop-down menu using its visible text.

    drop_down_menu.select_option("Price (high to low)")

    browser.close()

