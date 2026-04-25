

# Playwright assignments:

# Date: 29.03.2026
# Assignment - 11

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    customer_login_btn = page.get_by_text("Customer Login")
    customer_login_btn.click()

    drop_down_menu_your_name = page.locator('[class*="form-control"]')
    drop_down_menu_your_name.select_option(index=2)

    selected_option_text = drop_down_menu_your_name.locator("option:checked").text_content()
    assert selected_option_text.strip() == "Harry Potter", "Harry Potter was not selected."

    login_btn = page.locator('[class="btn btn-default"]')
    login_btn.click()

    deposit_option_btn = page.get_by_text("Deposit")
    deposit_option_btn.click()

    deposit_amount_input_box = page.locator('[class*="form-control"]')
    deposit_amount_input_box.fill("1000000")

    deposit_btn = page.locator('[class="btn btn-default"]')
    deposit_btn.click()

    browser.close()

