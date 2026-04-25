from python_course106_2026.introduction_to_playwright.page_object_model.pages.welcome_page import WelcomePage
from python_course106_2026.introduction_to_playwright.page_object_model.pages.product_page import ProductPage


def test_01_swag_labs_get_price_of_the_first_item_test(setup_playwright_swag_labs):
    print("\n*** Test - 01 ***")
    print("\nGo to the SwagLabs website.\n")
    page = setup_playwright_swag_labs

    page.goto(
        "https://www.saucedemo.com/",
        wait_until="domcontentloaded",
        timeout=60000
    )

    welcome_page = WelcomePage(page)
    product_page = ProductPage(page)

    welcome_page.swag_labs_website_set_login()
    product_page.swag_labs_website_get_price_of_the_first_item()


def test_02_swag_labs_set_drop_down_menu_test(setup_playwright_swag_labs):
    print("\n*** Test - 02 ***")
    print("\nGo to the SwagLabs website.\n")
    page = setup_playwright_swag_labs

    page.goto(
        "https://www.saucedemo.com/",
        wait_until="domcontentloaded",
        timeout=60000
    )

    welcome_page = WelcomePage(page)
    product_page = ProductPage(page)

    welcome_page.swag_labs_website_set_login()
    product_page.swag_labs_website_set_drop_down_menu()

