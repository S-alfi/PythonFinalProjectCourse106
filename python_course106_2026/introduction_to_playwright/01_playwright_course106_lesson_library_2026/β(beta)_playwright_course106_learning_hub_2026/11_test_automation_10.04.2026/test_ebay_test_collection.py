

def test_01_ebay_search_input_box_fill_test(setup_playwright):
    print("\n*** Test - 01 ***")
    print("\nGo to the eBay website.\n")
    page = setup_playwright

    page.goto("https://www.ebay.com/")

    search_input_box = page.locator('#gh-ac')
    search_input_box.click()
    search_input_box.fill("Sneakers")

    page.keyboard.press("Enter")


def test_02_ebay_advanced_button_click_test(setup_playwright):
    print("\n*** Test - 02 ***")
    print("\nGo to the eBay website.\n")
    page = setup_playwright

    page.goto("https://www.ebay.com/")

    advanced_button = page.get_by_role("link", name="Advanced")
    advanced_button.click()

    current_url = page.url
    print(f'The URL of the eBay advanced search page is: {current_url}\n')

