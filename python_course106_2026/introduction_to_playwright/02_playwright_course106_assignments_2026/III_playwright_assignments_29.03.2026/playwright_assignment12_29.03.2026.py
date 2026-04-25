

# Playwright assignments:

# Date: 29.03.2026
# Assignment - 12

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.calculator.net/interest-calculator.html")

    current_url = page.url
    assert current_url == "https://www.calculator.net/interest-calculator.html", "The current page URL is incorrect."

    initial_investment_input_box = page.locator('[id="cstartingprinciple"]')
    initial_investment_input_box.clear()
    initial_investment_input_box.fill("1250000")

    Annual_contribution_input_box = page.locator('[id="cannualaddition"]')
    Annual_contribution_input_box.clear()
    Annual_contribution_input_box.fill("100000")

    Monthly_contribution_input_box = page.locator('[id="cmonthlyaddition"]')
    Monthly_contribution_input_box.clear()
    Monthly_contribution_input_box.fill("50000")

    radio_btn_contribute_type = page.locator('label[for="cadditionat2"]')
    radio_btn_contribute_type.click()

    Interest_rate_input_box = page.locator('[id="cinterestrate"]')
    Interest_rate_input_box.clear()
    Interest_rate_input_box.fill("5")

    drop_down_menu_compound = page.locator('[name="ccompound"]')
    drop_down_menu_compound.select_option("continuously")

    investment_length_years_input_box = page.locator('[id="cyears"]')
    investment_length_years_input_box.clear()
    investment_length_years_input_box.fill("10")

    investment_length_months_input_box = page.locator('[id="cmonths"]')
    investment_length_months_input_box.clear()
    investment_length_months_input_box.fill("8")

    tax_rate_input_box = page.locator('[id="ctaxtrate"]')
    tax_rate_input_box.clear()
    tax_rate_input_box.fill("0")

    inflation_rate_input_box = page.locator('[id="cinflationrate"]')
    inflation_rate_input_box.clear()
    inflation_rate_input_box.fill("2")

    calculate_btn = page.locator('[name="x"]')
    calculate_btn.click()

    browser.close()

