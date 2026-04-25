import pytest
from playwright.sync_api import sync_playwright, expect

expect.set_options(timeout=10_000)

# What is a conftest file?

# A conftest.py file is a special configuration file used in the Python testing framework pytest
# that allows you to share test setup code (such as fixtures and configuration) across multiple test files automatically.


@pytest.fixture()
def setup_playwright():
    print("\n### Test start ###")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        # In pytest, yield is used within fixtures to separate the "Setup" code from the "Teardown" code.
        # Setup: Everything before the yield statement runs before the test starts.
        # Teardown: Everything after the yield statement runs after the test is finished, regardless of whether the test passed or failed.

        yield page
        print("### Test end ###\n")
        page.close()
        browser.close()

