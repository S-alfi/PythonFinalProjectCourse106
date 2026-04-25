

# Playwright assignments:

# Date: 17.04.2026
# Assignment - 14

def test_01_nike_search_for_more_than_one_store_in_a_city_test(setup_playwright):
    print("\n*** Test - 01 ***")
    print("\nGo to the Nike website.\n")
    page = setup_playwright

    # This line of code acts as if you clicked "Block" or "Deny" on the popup instantly.
    # Granting permission to an empty list ([]) is equivalent to granting no permissions at all.

    context = page.context
    context.grant_permissions([], origin="https://www.nike.com")

    page.goto(
        "https://www.nike.com/il/",
        wait_until="domcontentloaded",
        timeout=60000
    )

    find_a_store_btn = page.get_by_role("link", name="Find a Store").first
    find_a_store_btn.click()

    search_location_input_box = page.locator('#ta-Location_input')
    search_location_input_box.fill("New York")
    search_location_input_box.click()
    page.keyboard.press("Enter")

    stores = page.locator('section[class*="border-bottom"]')
    stores.first.wait_for(timeout=10000)
    store_count = stores.count()
    print(f"{store_count} stores found.\n")
    assert store_count > 1, f"Expected more than one store, but found {store_count}"


def test_02_calculator_dot_net_make_a_calculation_test(setup_playwright):
    print("\n*** Test - 02 ***")
    print("\nGo to the Calculator.net website.\n")
    page = setup_playwright

    page.goto(
        "https://www.calculator.net/",
        wait_until="domcontentloaded",
        timeout=60000
    )

    grade_calculator_btn = page.get_by_role("link", name="Grade Calculator")
    grade_calculator_btn.click()

    midterm_exam_grade = page.locator('[name="s3"]')
    midterm_exam_grade.clear()
    midterm_exam_grade.fill("23")

    calculate_btn = page.locator('input[name="x"]').first
    calculate_btn.click()

    result = page.locator('p[class="verybigtext"]').inner_text()
    print(f'{result}\n')

    c_index = result.index("C")
    final_result = result[c_index:]
    print(f'{final_result}\n')


def test_03_xyz_bank_login_with_css_test(setup_playwright):
    print("\n*** Test - 03 ***")
    print("\nGo to the XYZ Bank website.\n")
    page = setup_playwright

    page.goto(
        "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login",
        wait_until="domcontentloaded",
        timeout=60000
    )

    customer_login_btn = page.locator('button[class="btn btn-primary btn-lg"]').first
    customer_login_btn.click()


def test_04_sv_burger_make_a_signup_test(setup_playwright):
    print("\n*** Test - 04 ***")
    print("\nGo to the SVBurger website.\n")
    page = setup_playwright

    page.goto(
        "https://svburger1.co.il/#/SignUp",
        wait_until="domcontentloaded",
        timeout=60000
    )

    signup_field = page.query_selector_all('input[class="form-control"]')

    first_name_input_box = signup_field[0]
    first_name_input_box.fill("Elon")

    last_name_input_box = signup_field[1]
    last_name_input_box.fill("Musk")

    email_input_box = signup_field[2]
    email_input_box.fill("example_email@gmail.com")

    password_input_box = signup_field[3]
    password_input_box.fill("TestingSvBurger2026")

    confirm_password_input_box = signup_field[4]
    confirm_password_input_box.fill("TestingSvBurger2026")

    signup_btn = page.get_by_role("button", name="Sign Up")
    signup_btn.click()

