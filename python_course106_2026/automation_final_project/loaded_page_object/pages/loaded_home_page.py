

class LoadedHomePage:
    def __init__(self, page):
        print("\n### Home Page ###\n")
        self.page = page


    def loaded_home_page_search(self):

        # Validate that the loaded page URL matches the expected homepage

        current_url = self.page.url
        assert current_url == "https://www.loaded.com/", "The current page URL is incorrect."

        # Enter 'Elden Ring' into the search input box and click the search button

        self.page.wait_for_selector('#search')

        search_input_box = self.page.locator('#search')
        search_input_box.click()
        search_input_box.press_sequentially("Elden Ring", delay=100)

        self.page.wait_for_selector('button[type="submit"]')

        magnifying_glass_search_btn = self.page.locator('button[type="submit"][class="absolute top-1.5 left-3 text-black"]')
        magnifying_glass_search_btn.click()


    def loaded_set_drop_down_menu(self):

        # Click the Relevance dropdown menu

        relevance_drop_down_menu = self.page.locator('div[id="algolia-sorts"]')
        relevance_drop_down_menu.click()

        # Select the 'Highest price' option from the Relevance dropdown menu

        self.page.wait_for_selector('div[class="select-items select-hide ais-Panel-body"]', state="visible")

        relevance_drop_down_menu_options = self.page.locator('div[class="select-items select-hide ais-Panel-body"] div')
        relevance_drop_down_menu_target_option = relevance_drop_down_menu_options.nth(2)
        relevance_drop_down_menu_target_option.wait_for(state="visible")
        relevance_drop_down_menu_target_option.click()

        # Click the Platform dropdown menu

        platform_drop_down_menu = self.page.locator('div[class="ais-Panel-header"]').nth(0)
        platform_drop_down_menu.click()

        # Select the 'Steam' checkbox from the Platform dropdown menu

        platform_drop_down_menu_target_option = self.page.get_by_role("checkbox", name="Steam")
        platform_drop_down_menu_target_option.click()

        # Click the Region dropdown menu

        region_drop_down_menu = self.page.locator('div[class="ais-Panel-header"]').nth(1)
        region_drop_down_menu.click()

        # Select the 'Europe Middle East and Africa' checkbox from the Region dropdown menu

        region_drop_down_menu_target_option = self.page.get_by_role("checkbox", name="Europe Middle East and Africa")
        region_drop_down_menu_target_option.click()

        # Click the Language dropdown menu

        language_drop_down_menu = self.page.locator('div[class="ais-Panel-header"]').nth(3)
        language_drop_down_menu.click()

        # Select the 'English' checkbox from the Language dropdown menu

        language_drop_down_menu_target_option = self.page.get_by_role("checkbox", name="English")
        language_drop_down_menu_target_option.click()

        # Click the search input box

        search_input_box = self.page.locator('#search')
        search_input_box.click()


    def loaded_set_currency(self):

        # Click the set currency button

        set_currency_btn = self.page.locator('button[type="button"][class="currency-toggle max-md:text-sm gtm"]')
        set_currency_btn.click()

        # Set the Loaded website currency to 'USD'

        selected_currency = self.page.locator('[class="switcher-dropdown"]').get_by_role("link", name="USD", exact=True).first
        clean_selected_currency = selected_currency.inner_text().replace("\n", " ")
        selected_currency.click()
        print(f'The Loaded website currency updated to: [{clean_selected_currency}]\n')

