

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("http://www.ebay.com")

    search_input_box = page.locator('#gh-ac')
    search_input_box.click()
    search_input_box.fill("Sneakers")

    # page.keyboard.press() is a method from Playwright used to simulate pressing a key on the keyboard.

    page.keyboard.press("Enter")

    browser.close()

