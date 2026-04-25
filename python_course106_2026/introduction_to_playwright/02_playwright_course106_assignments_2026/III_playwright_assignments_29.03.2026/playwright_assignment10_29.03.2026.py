

# Playwright assignments:

# Date: 29.03.2026
# Assignment - 10

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://demo.guru99.com/test/newtours/reservation.php")

    radio_btn_trip_type = page.locator('input[name="tripType"][value="oneway"]')
    radio_btn_trip_type.check()

    drop_down_menu_passengers = page.locator('[name="passCount"]')
    drop_down_menu_passengers.select_option(index=0)

    drop_down_menu_departing_from = page.locator('[name="fromPort"]')
    drop_down_menu_departing_from.select_option("New York")

    drop_down_menu_on_date_month = page.locator('[name="fromMonth"]')
    drop_down_menu_on_date_month.select_option("April")

    drop_down_menu_on_date_day = page.locator('[name="fromDay"]')
    drop_down_menu_on_date_day.select_option("19")

    drop_down_menu_arriving_in = page.locator('[name="toPort"]')
    drop_down_menu_arriving_in.select_option("London")

    drop_down_menu_returning_date_month = page.locator('[name="toMonth"]')
    drop_down_menu_returning_date_month.select_option("May")

    drop_down_menu_returning_date_day = page.locator('[name="toDay"]')
    drop_down_menu_returning_date_day.select_option("19")

    radio_btn_service_class = page.locator('input[name="servClass"][value="First"]')
    radio_btn_service_class.check()

    drop_down_menu_airline = page.locator('[name="airline"]')
    selected_value = drop_down_menu_airline.input_value()

    assert selected_value == "No Preference", "The selected option does not match the expected value."

    continue_btn = page.locator('[name="findFlights"]')
    continue_btn.click()

    browser.close()

