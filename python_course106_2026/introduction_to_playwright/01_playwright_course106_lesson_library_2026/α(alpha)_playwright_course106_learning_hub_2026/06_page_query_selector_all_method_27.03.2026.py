

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")

    user_name = page.locator('[name="user-name"]')
    user_name.click()
    user_name.clear()
    user_name.fill("standard_user")

    password = page.locator('[name="password"]')
    password.click()
    password.clear()
    password.fill("secret_sauce")

    login_button = page.locator('[name="login-button"]')
    login_button.click()

    print()

    # [Important]: If the class attribute contains multiple class names separated by spaces,
    # Replace each space with a dot (.) when using it as a selector - but only if your original command doesn’t work.

    # An example: ('[class="inventory item price"]') → ('[class="inventory.item.price"]').

    # page.query_selector_all() is a method from Playwright that returns a list of all elements on the page that match a given CSS selector.

    # An example: page.query_selector_all('[class="inventory_item_price"]') returns a list of all elements that have the class inventory_item_price.

    price_list = page.query_selector_all('[class="inventory_item_price"]')
    first_price = price_list[0]
    first_price_inner_text = first_price.inner_text()
    print(f' The price of the first item is: {first_price_inner_text}')

    print()

    prices_above_25 = []

    for i, price in enumerate(price_list, start=1):
        price_inner_text = price.inner_text()
        price_inner_text_replaced = price_inner_text.replace("$", "")

        # An example of float variable, A float is a type of number that has a decimal point.

        price_inner_text_replaced_casting_to_float = float(price_inner_text_replaced)
        print(f' The price for item number -> ({i}), is:  {price_inner_text_replaced_casting_to_float}')

        if price_inner_text_replaced_casting_to_float > 25:
            prices_above_25.append((i, price_inner_text_replaced_casting_to_float))

    print()

    print(" The items with prices above 25$ are:")
    for item_number, price in prices_above_25:
        print(f' Item number -> ({item_number}), is: {price}')

    browser.close()

