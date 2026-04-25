

def test_01_swag_labs_login_test(setup_playwright):
    print("\n*** Test - 01 ***")
    print("\nGo to the SwagLabs website.\n")
    page = setup_playwright

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

