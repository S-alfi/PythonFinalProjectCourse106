from python_course106_2026.automation_final_project.loaded_page_object.pages.loaded_home_page import LoadedHomePage

from python_course106_2026.automation_final_project.loaded_page_object.pages.loaded_latest_games_page import \
    LoadedLatestGamesPage

from python_course106_2026.automation_final_project.loaded_page_object.pages.loaded_help_center_page import \
    LoadedHelpCenterPage



def test_home_page_search_and_dropdown_navigation(setup_playwright_loaded_website):
    """
    Test Case: Fill the search input box and interact with the drop-down menus on the Home Page.
    """
    print("\n*** Running Test - 01 ***")
    page = setup_playwright_loaded_website

    page.goto(
        "https://www.loaded.com",
        wait_until="networkidle",
        timeout=60000
    )

    loaded_home_page = LoadedHomePage(page)
    loaded_home_page.search_for_game()
    loaded_home_page.apply_and_verify_search_filters()


def test_currency_updates_to_usd(setup_playwright_loaded_website):
    """
    Test Case: Set the Loaded website currency to USD globally.
    """
    print("\n*** Running Test - 02 ***")
    page = setup_playwright_loaded_website

    page.goto(
        "https://www.loaded.com",
        wait_until="networkidle",
        timeout=60000
    )

    loaded_home_page = LoadedHomePage(page)
    loaded_home_page.set_currency_to_usd()


def test_sort_and_extract_top_five_unique_games(setup_playwright_loaded_website):
    """
    Test Case: Navigate to the Latest Games page, toggle region, and sort to find the top 5 unique games.
    """
    print("\n*** Running Test - 03 ***")
    page = setup_playwright_loaded_website

    page.goto(
        "https://www.loaded.com",
        wait_until="networkidle",
        timeout=60000
    )

    loaded_home_page = LoadedHomePage(page)
    loaded_home_page.set_currency_to_usd()

    loaded_latest_games_page = LoadedLatestGamesPage(page)
    loaded_latest_games_page.navigate_to_latest_games_page()
    loaded_latest_games_page.toggle_region()
    loaded_latest_games_page.verify_top_5_unique_games()


def test_pre_order_first_available_item(setup_playwright_loaded_website):
    """
    Test Case: Navigate to the Latest Games page and pre-order the first item.
    """
    print("\n*** Running Test - 04 ***")
    page = setup_playwright_loaded_website

    page.goto(
        "https://www.loaded.com",
        wait_until="networkidle",
        timeout=60000
    )

    loaded_home_page = LoadedHomePage(page)
    loaded_home_page.set_currency_to_usd()

    loaded_latest_games_page = LoadedLatestGamesPage(page)
    loaded_latest_games_page.navigate_to_pre_order_section()
    loaded_latest_games_page.pre_order_first_item_and_proceed_to_checkout()


def test_help_center_search_functionality(setup_playwright_loaded_website):
    """
    Test Case: Navigate to the Help Center page and perform a search.
    """
    print("\n*** Running Test - 05 ***")
    page = setup_playwright_loaded_website

    page.goto(
        "https://www.loaded.com",
        wait_until="networkidle",
        timeout=60000
    )

    loaded_help_center_page = LoadedHelpCenterPage(page)
    loaded_help_center_page.navigate_to_help_center_page()
    loaded_help_center_page.search_for_legal_documents()

