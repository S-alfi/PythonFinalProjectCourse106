import pytest
from playwright.sync_api import sync_playwright, expect

expect.set_options(timeout=10_000)

@pytest.fixture()
def setup_playwright_swag_labs():
    print("\n### Test start ###")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()


        yield page
        print("\n### Test end ###\n")
        page.close()
        browser.close()

