from python_course106_2026.automation_final_project.loaded_page_object.pages.loaded_home_page import LoadedHomePage

from python_course106_2026.automation_final_project.loaded_page_object.pages.loaded_latest_games_page import \
    LoadedLatestGamesPage

from python_course106_2026.automation_final_project.loaded_page_object.pages.loaded_pre_order_page import \
    LoadedPreOrderPage

from python_course106_2026.automation_final_project.loaded_page_object.pages.loaded_help_center_page import \
    LoadedHelpCenterPage



def test_01_loaded_home_page_search_input_box_fill_test(setup_playwright_loaded_website):
    """
    Test Case: Fill the search input box and interact with the drop-down menu on the Home Page.
    """
    print("\n*** Running Test - 01: Home Page Search ***")
    page = setup_playwright_loaded_website

    page.goto(
        "https://www.loaded.com",
        wait_until="networkidle",
        timeout=60000
    )

    loaded_home_page = LoadedHomePage(page)
    loaded_home_page.loaded_home_page_search()
    loaded_home_page.loaded_set_drop_down_menu()


def test_02_loaded_home_page_set_currency_to_usd_test(setup_playwright_loaded_website):
    """
    Test Case: Set the global site currency to USD on the Home Page.
    """
    print("\n*** Running Test - 02: Home Page Set Currency to USD ***")
    page = setup_playwright_loaded_website

    page.goto(
        "https://www.loaded.com",
        wait_until="networkidle",
        timeout=60000
    )

    loaded_home_page = LoadedHomePage(page)
    loaded_home_page.loaded_set_currency()


def test_03_loaded_latest_games_page_search_for_the_top_5_games_test(setup_playwright_loaded_website):
    """
    Test Case: Navigate to Latest Games page, toggle region, and sort to find the top 5 games.
    """
    print("\n*** Running Test - 03: Latest Games Page Search For Top 5 Games ***")
    page = setup_playwright_loaded_website

    page.goto(
        "https://www.loaded.com",
        wait_until="networkidle",
        timeout=60000
    )

    loaded_home_page = LoadedHomePage(page)
    loaded_home_page.loaded_set_currency()

    loaded_latest_games_page = LoadedLatestGamesPage(page)
    loaded_latest_games_page.loaded_navigate_to_the_latest_games_page()
    loaded_latest_games_page.loaded_click_region_toggle_button()
    loaded_latest_games_page.loaded_sort_top_5_games()


def test_04_loaded_pre_order_page_pre_order_first_item_test(setup_playwright_loaded_website):
    """
    Test Case: Navigate to Pre-Order page, toggle region, and pre-order the first item.
    """
    print("\n*** Running Test - 04: Pre-Order Page Pre-Order First Item ***")
    page = setup_playwright_loaded_website

    page.goto(
        "https://www.loaded.com",
        wait_until="networkidle",
        timeout=60000
    )

    loaded_home_page = LoadedHomePage(page)
    loaded_home_page.loaded_set_currency()

    loaded_pre_order_page = LoadedPreOrderPage(page)
    loaded_pre_order_page.loaded_navigate_to_the_pre_order_page()
    loaded_pre_order_page.loaded_click_region_toggle_button()
    loaded_pre_order_page.loaded_pre_order_first_item()


def test_05_loaded_help_center_page_search_test(setup_playwright_loaded_website):
    """
    Test Case: Navigate to Help Center page and perform a search.
    """
    print("\n*** Running Test - 05: Help Center Page Search ***")
    page = setup_playwright_loaded_website

    page.goto(
        "https://www.loaded.com",
        wait_until="networkidle",
        timeout=60000
    )

    loaded_help_center_page = LoadedHelpCenterPage(page)
    loaded_help_center_page.loaded_navigate_to_the_help_center_page()
    loaded_help_center_page.loaded_help_center_page_search()

