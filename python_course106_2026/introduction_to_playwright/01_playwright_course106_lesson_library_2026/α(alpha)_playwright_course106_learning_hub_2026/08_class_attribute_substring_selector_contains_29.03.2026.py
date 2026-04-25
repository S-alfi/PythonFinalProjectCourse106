

# Check for the shopping bag button to contain 0 as default.

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.zara.com/il/en/")

    shopping_bag_btn_01 = page.locator('[class="layout-actionable link"]').all()[0]

    # Using [class*="…"] selects all elements whose class attribute contains the specified text.

    # An example: page.locator('[class*="layout-actionable"]') gets all the class elements that starts with "layout-actionable".

    shopping_bag_btn_02 = page.locator('[class*="layout-actionable"]').all()[1]
    shopping_bag_btn_02_inner_text = shopping_bag_btn_02.inner_text()

    # Version 01
    # Get the number 0 with the index of the word 'bag' + 3.

    index_of_bag = shopping_bag_btn_02_inner_text.index("bag")
    bag_with_count_count_number_01 = shopping_bag_btn_02_inner_text[index_of_bag+3:]
    print(f' \nGet the value of shopping bag (0), Version 01: {bag_with_count_count_number_01}')

    # Version 02
    # Get the number 0 with the index[-1:], returns the last element counting from the end.

    bag_with_count_count_number_02 = shopping_bag_btn_02_inner_text[-1:]
    print(f' \nGet the value of shopping bag (0), Version 02: {bag_with_count_count_number_02}')

    browser.close()

