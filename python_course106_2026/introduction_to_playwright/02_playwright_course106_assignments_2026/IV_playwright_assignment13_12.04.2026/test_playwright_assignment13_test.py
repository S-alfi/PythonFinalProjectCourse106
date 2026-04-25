import time

# Playwright assignments:

# Date: 12.04.2026
# Assignment - 13

def test_01_zara_search_for_shirt_in_first_product_name_test(setup_playwright):
    print("\n*** Test - 01 ***")
    print("\nGo to the Zara website.\n")
    page = setup_playwright

    page.goto(
        "https://www.zara.com/il/en/",
        wait_until="domcontentloaded",
        timeout=60000
    )

    search_btn = page.get_by_role("link", name="Search")
    search_btn.click()

    page.wait_for_selector('[id="search-home-form-combo-input"]')

    search_input_box = page.locator('[id="search-home-form-combo-input"]')
    search_input_box.clear()
    search_input_box.fill("Shirt")
    page.keyboard.press("Enter")

    time.sleep(5)

    products = page.locator('[class="product-link _item product-grid-product-info__name link"]')
    assert products.count() > 0, "No products found."

    first_product_name = products.first.text_content()
    print(f"First product name: {first_product_name}\n")
    assert "shirt" in first_product_name.lower(), f"Expected 'shirt' in product name, got: {first_product_name}"


def test_02_nike_search_for_href_buttons_for_men_and_women_test(setup_playwright):
    print("\n*** Test - 02 ***")
    print("\nGo to the Nike website.\n")
    page = setup_playwright

    page.goto(
        "https://www.nike.com/il/",
        wait_until="domcontentloaded",
        timeout=60000
    )

    men_btn = page.get_by_role("link", name="Men", exact=True).first
    assert men_btn.text_content() == "Men", f"Expected 'Men' button, got: {men_btn.text_content()}"

    women_btn = page.get_by_role("link", name="Women", exact=True).first
    assert women_btn.text_content() == "Women", f"Expected 'Women' button, got: {women_btn.text_content()}"


def test_03_nike_search_for_something_in_the_help_page_test(setup_playwright):
    print("\n*** Test - 03 ***")
    print("\nGo to the Nike website.\n")
    page = setup_playwright

    page.goto(
        "https://www.nike.com/il/",
        wait_until="domcontentloaded",
        timeout=60000
    )

    help_btn = page.get_by_role("link", name="Help").first
    help_btn.click()

    page.wait_for_selector('#searchInput')

    search_text = "What is Nike's returns policy"
    get_help_input_box = page.locator('#searchInput')
    get_help_input_box.clear()
    get_help_input_box.press_sequentially(search_text, delay=100)

    if get_help_input_box.input_value() != search_text:
        get_help_input_box.fill(search_text)

    page.keyboard.press("Enter")

    print(f"The value entered into the ‘Get Help’ input box is: {get_help_input_box.input_value()}\n")

