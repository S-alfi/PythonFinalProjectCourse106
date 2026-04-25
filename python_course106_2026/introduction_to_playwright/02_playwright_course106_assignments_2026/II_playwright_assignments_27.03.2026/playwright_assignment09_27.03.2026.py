

# Playwright assignments:

# Date: 27.03.2026
# Assignment - 09

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.zara.com/il/en/")

    # Check for the shopping bag button to contain 0 as default.

    shopping_bag_btn = page.locator('[class="layout-actionable link"]').all()[0]
    shopping_bag_btn_inner_text = shopping_bag_btn.inner_text()

    # Get the number 0 with the index[-1:], returns the last element counting from the end.

    bag_with_count_count_number = shopping_bag_btn_inner_text[-1:]
    print(f' \nGet the value of shopping bag (0), The value = {bag_with_count_count_number}')

    browser.close()

