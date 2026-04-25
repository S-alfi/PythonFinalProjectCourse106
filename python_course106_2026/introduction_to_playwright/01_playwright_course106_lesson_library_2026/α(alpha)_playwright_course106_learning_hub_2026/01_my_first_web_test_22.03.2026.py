

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("http://www.ebay.com")

    # A shortcut for the id attribute is: ('#(X)').

    search_input_box = page.locator('#gh-ac') # ('[id = "gh-ac"]') == ('#gh-ac')
    search_input_box.click()
    search_input_box.clear()
    search_input_box.fill("Phone")

    search_button = page.locator('#gh-search-btn')
    search_button.click()

    browser.close()

