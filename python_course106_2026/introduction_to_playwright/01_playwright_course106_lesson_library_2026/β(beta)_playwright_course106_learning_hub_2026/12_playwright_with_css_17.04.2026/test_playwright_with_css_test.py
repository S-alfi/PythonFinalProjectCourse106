

def test_01_swag_labs_login_with_css_test(setup_playwright):
    print("\n*** Test - 01 ***")
    print("\nGo to the SwagLabs website.\n")
    page = setup_playwright

    page.goto(
        "https://www.saucedemo.com/",
        wait_until="domcontentloaded",
        timeout=60000
    )

    user_name = page.locator('input[id="user-name"][class*="input_error"]').first
    user_name.click()
    user_name.clear()
    user_name.fill("standard_user")

    password = page.locator('input[id="password"][class*="input_error"]').last
    password.click()
    password.clear()
    password.fill("secret_sauce")

    login_button = page.locator('input[type="submit"][class="submit-button btn_action"]')
    login_button.click()

