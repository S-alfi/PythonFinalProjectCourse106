

class LoadedHomePage:
    def __init__(self, page):
        print("\n### Home Page ###\n")
        self.page = page


    def search_for_game(self):

        # Validate that the Loaded page URL matches the expected Home Page

        home_page_url = self.page.url
        assert home_page_url == "https://www.loaded.com/", "The current page URL is incorrect."

        # Enter 'Elden Ring' into the search input box

        self.page.wait_for_selector('#search')

        home_page_search_input_box = self.page.locator('#search')
        home_page_search_input_box.clear()
        home_page_search_input_box.press_sequentially("Elden Ring", delay=100)


    def apply_and_verify_search_filters(self):

        # Click the Relevance dropdown menu

        relevance_drop_down_menu = self.page.locator('div[id="algolia-sorts"]')
        relevance_drop_down_menu.click()

        # Select the 'Highest price' option from the Relevance dropdown menu

        self.page.wait_for_selector('div[class="select-items select-hide ais-Panel-body"]', state="visible")

        relevance_drop_down_menu_options = self.page.locator('div[class="select-items select-hide ais-Panel-body"] div')
        relevance_drop_down_menu_target_option = relevance_drop_down_menu_options.nth(2)
        target_option_text = relevance_drop_down_menu_target_option.inner_text().strip()
        relevance_drop_down_menu_target_option.wait_for(state="visible")
        relevance_drop_down_menu_target_option.click()
        assert target_option_text == "Highest price", f"Expected 'Highest price' but found '{target_option_text}'."

        # Click the Platform dropdown menu

        platform_drop_down_menu = self.page.locator('div[class="ais-Panel-header"]').nth(0)
        platform_drop_down_menu.click()

        # Select the 'Steam' checkbox from the Platform dropdown menu

        platform_drop_down_menu_target_option = self.page.get_by_role("checkbox", name="Steam")
        platform_drop_down_menu_target_option.click()
        assert platform_drop_down_menu_target_option.is_checked() == True,\
            f"Expected the 'Steam' platform checkbox to be selected, but it remained unchecked."

        # Click the Region dropdown menu

        region_drop_down_menu = self.page.locator('div[class="ais-Panel-header"]').nth(1)
        region_drop_down_menu.click()

        # Select the 'Europe Middle East and Africa' checkbox from the Region dropdown menu

        region_drop_down_menu_target_option = self.page.get_by_role("checkbox", name="Europe Middle East and Africa")
        region_drop_down_menu_target_option.click()
        assert region_drop_down_menu_target_option.is_checked() == True,\
            f"Expected the 'Europe Middle East and Africa' region checkbox to be selected, but it remained unchecked."

        # Click the Language dropdown menu

        language_drop_down_menu = self.page.locator('div[class="ais-Panel-header"]').nth(3)
        language_drop_down_menu.click()

        # Select the 'English' checkbox from the Language dropdown menu

        language_drop_down_menu_target_option = self.page.get_by_role("checkbox", name="English")
        language_drop_down_menu_target_option.click()
        assert language_drop_down_menu_target_option.is_checked() == True,\
            f"Expected the 'English' language checkbox to be selected, but it remained unchecked."

        # Click the search input box

        home_page_search_input_box = self.page.locator('#search')
        home_page_search_input_box.click()


    def set_currency_to_usd(self):

        # Click the set currency button

        set_currency_btn = self.page.locator('button[type="button"][class="currency-toggle max-md:text-sm gtm"]')
        set_currency_btn.click()

        # Set the Loaded website currency to 'USD'

        selected_currency = self.page.locator('[class="switcher-dropdown"]').get_by_role("link", name="USD", exact=True).first
        clean_selected_currency = selected_currency.inner_text().replace("\n", " ")
        selected_currency.click()
        updated_currency_text = set_currency_btn.inner_text()
        assert "USD" in updated_currency_text, f"Currency update failed! Expected 'USD' but found '{updated_currency_text}'."
        print(f'The Loaded website currency updated to: [{clean_selected_currency}]\n')

