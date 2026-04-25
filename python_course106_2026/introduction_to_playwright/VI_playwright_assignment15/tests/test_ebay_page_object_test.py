from python_course106_2026.introduction_to_playwright.VI_playwright_assignment15.pages.ebay_home_page import \
    EbayHomePage

from python_course106_2026.introduction_to_playwright.VI_playwright_assignment15.pages.ebay_advanced_search_page import \
    EbayAdvancedSearchPage


def test_01_ebay_search_input_box_fill_test(setup_playwright_ebay):
    print("\n*** Test - 01 ***")
    print("\nGo to the eBay website.\n")
    page = setup_playwright_ebay

    page.goto(
        "https://www.ebay.com/",
        wait_until="domcontentloaded",
        timeout=60000
    )

    ebay_home_page = EbayHomePage(page)
    ebay_home_page.ebay_search_input_box_fill()


def test_02_ebay_advanced_button_click_test(setup_playwright_ebay):
    print("\n*** Test - 02 ***")
    print("\nGo to the eBay website.\n")
    page = setup_playwright_ebay

    page.goto(
        "https://www.ebay.com/",
        wait_until="domcontentloaded",
        timeout=60000
    )

    ebay_advanced_page = EbayAdvancedSearchPage(page)
    ebay_advanced_page.ebay_advanced_button_click()


def test_03_ebay_search_for_something_within_the_advanced_search_page_test(setup_playwright_ebay):
    print("\n*** Test - 03 ***")
    print("\nGo to the eBay website.\n")
    page = setup_playwright_ebay

    page.goto(
        "https://www.ebay.com/",
        wait_until="domcontentloaded",
        timeout=60000
    )

    ebay_advanced_page = EbayAdvancedSearchPage(page)
    ebay_advanced_page.ebay_advanced_button_click()
    ebay_advanced_page.ebay_search_for_something_within_the_advanced_search_page()

