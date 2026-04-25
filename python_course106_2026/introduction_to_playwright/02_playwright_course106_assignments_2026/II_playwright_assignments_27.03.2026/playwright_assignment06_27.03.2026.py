

# Playwright assignments:

# Date: 27.03.2026
# Assignment - 06

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    page.wait_for_selector("button.btn.btn-primary.btn-lg")

    buttons = page.query_selector_all('[class="btn btn-primary btn-lg"]')
    if len(buttons) > 1:
        bank_manager_login_btn = buttons[1]
        bank_manager_login_btn.click()
    else:
        print("Bank Manager Login button not found.")

    browser.close()

