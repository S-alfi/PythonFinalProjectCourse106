

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("http://www.ebay.com")

    search_input_box = page.locator('#gh-ac')
    search_input_box.click()
    search_input_box.fill("Sneakers")

    # The first() method selects the first element from a set of elements that match a given locator.
    # The variable search_button_first is assigned the first button element on the page whose accessible name is “Search”.

    search_button_first = page.get_by_role("button", name = "Search").first

    # The last() method selects the last element from a set of elements that match a given locator.
    # The variable search_button_last is assigned the last button element on the page whose accessible name is “Search”.

    search_button_last = page.get_by_role("button", name="Search").last

    # The nth(index) method selects a single element from a set of matched elements based on its position, where indexing starts at 0 (for example, nth(0) returns the first element).
    # The variable search_button_nth is assigned the second button element on the page whose accessible name is “Search”, index = 1.

    search_button_nth = page.get_by_role("button", name="Search").nth(1)

    # The all() method returns all elements from a group of matched elements as a list.
    # The variable search_button_as_list is assigned a list of all button elements on the page whose accessible name is “Search”.

    search_button_list = page.get_by_role("button", name="Search").all()

    browser.close()

