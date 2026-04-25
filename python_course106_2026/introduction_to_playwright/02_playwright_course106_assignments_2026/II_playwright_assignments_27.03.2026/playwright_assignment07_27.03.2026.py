

# Playwright assignments:

# Date: 27.03.2026
# Assignment - 07

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.nike.com/il/")

    sport_btn = page.get_by_role("link", name="Sport")
    sport_btn.click()

    browser.close()

