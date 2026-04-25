

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("http://www.ebay.com")

    # page.get_by_role() is a method from Playwright used to locate elements on a page based on their ARIA role and accessible name.
    # ARIA stands for Accessible Rich Internet Applications.

    # An example: The “Advanced” button is implemented as a link and has the accessible name “Advanced”.

    advanced_button = page.get_by_role("link" , name="Advanced")
    advanced_button.click()

    browser.close()

