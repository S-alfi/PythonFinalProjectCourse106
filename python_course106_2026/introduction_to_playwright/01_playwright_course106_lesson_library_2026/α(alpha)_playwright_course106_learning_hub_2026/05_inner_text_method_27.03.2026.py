import time

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://advantageonlineshopping.com/#/")

    contact_us_button = page.get_by_role("link" , name="CONTACT US")
    time.sleep(8) # Pause for 8 seconds
    contact_us_button.click()

    # .inner_text() is a method from Playwright used to retrieve the visible text content of an element on a web page.

    # An example: Get the visible text of the "CONTACT US" button = "CONTACT US".

    contact_us_button_inner_text = contact_us_button.inner_text()
    print(f' \nThe "CONTACT US" button value = {contact_us_button_inner_text}')

    browser.close()

