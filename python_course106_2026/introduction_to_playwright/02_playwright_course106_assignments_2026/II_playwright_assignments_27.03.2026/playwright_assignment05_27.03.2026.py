

# Playwright assignments:

# Date: 27.03.2026
# Assignment - 05

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://ecommerce-playground.lambdatest.io/")

    search_input_box = page.get_by_role("textbox", name="Search For Products")
    search_input_box.fill("iPhone")
    page.keyboard.press("Enter")

    browser.close()

