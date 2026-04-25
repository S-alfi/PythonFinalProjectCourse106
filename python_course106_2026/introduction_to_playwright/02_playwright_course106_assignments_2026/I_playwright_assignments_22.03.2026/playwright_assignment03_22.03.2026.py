

# Playwright assignments:

# Date: 22.03.2026
# Assignment - 03

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Go to "http://www.ebay.com" and click the "Advanced" button

    page.goto("http://www.ebay.com")

    advanced_btn = page.get_by_text("Advanced")
    advanced_btn.click()

    # Check the current URL and print it.

    current_url = page.url
    print(current_url)

    browser.close()

