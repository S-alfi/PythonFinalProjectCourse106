

class LoadedLatestGamesPage:
    def __init__(self, page):
        print("\n### Latest Games Page ###\n")
        self.page = page


    def navigate_to_latest_games_page(self):

        # Navigate to the Latest Games page

        latest_games_btn = self.page.get_by_role("link", name="Latest Games", exact=True)
        latest_games_btn.click()

        # Validate that the Loaded page URL matches the expected Latest Games page

        latest_games_page_url = self.page.url
        assert "latest-games" in latest_games_page_url, f"Expected 'latest-games' in {latest_games_page_url}"


    def navigate_to_pre_order_section(self):

        # Navigate to the Pre-Order section within the Latest Games page

        pre_order_btn = self.page.get_by_role("link", name="Pre-Order", exact=True)
        pre_order_btn.click()


    def toggle_region(self):

        # Switch between Global and Local region settings to update the game list.

        self.page.wait_for_selector('span[class="switch-label"]', state="visible", timeout=10000)

        region_switch_btn = self.page.locator('[class="switch-label"]')
        region_switch_btn.click()
        self.page.wait_for_timeout(3000)


    def verify_top_5_unique_games(self):
        """
        The verify_top_5_unique_games function:

        Identifies the top 5 unique game franchises from the results.

        Filters out duplicate titles from the same IP (e.g., different editions of the same game)
        to ensure the list contains five distinct titles with their prices.
        """

        latest_games_top_5_games_list = []
        seen_core_names = set()

        self.page.wait_for_selector('div[class="product-info"]', state="visible", timeout=10000)

        products = self.page.query_selector_all('div[class="product-info"]')
        assert len(products) > 0, "No products found on the page!"

        for product in products:

            title_element = product.query_selector('a[class="product-item-link text-sm gtm"]')
            price_element = product.query_selector('span[class="price"]')

            if not title_element:
                continue

            raw_title = title_element.text_content()
            if not raw_title:
                continue

            game_title = raw_title.strip().upper()
            game_price = price_element.text_content().strip() if price_element else "N/A"

            words = game_title.split()
            base_game_ip = words[0] if words else game_title

            if base_game_ip not in seen_core_names:
                latest_games_top_5_games_list.append(f"{game_title} - {game_price}")
                seen_core_names.add(base_game_ip)

            if len(latest_games_top_5_games_list) == 5:
                break

        assert len(latest_games_top_5_games_list) == 5, f"Expected 5 games, but only found {len(latest_games_top_5_games_list)}."

        print("Top 5 games:\n")

        for index, game in enumerate(latest_games_top_5_games_list, start=1):
            print(f"{index}. {game}")


    def pre_order_first_item_and_proceed_to_checkout(self):

        self.page.wait_for_url("**/latest-games?status=preorders**", timeout=10000)

        # Click the first item in the Pre-Order section

        first_item = self.page.locator('div[class="product-info"] a >> visible=true').first
        first_item.scroll_into_view_if_needed()
        clean_first_item = first_item.inner_text().strip()
        first_item.click()

        # Click the Pre-Order button to be redirected to the Checkout Page

        pre_order_btn = self.page.locator('#product-buynow-button')
        pre_order_btn.wait_for(state="visible", timeout=10000)
        pre_order_btn.click()

        # Verify that the Pre-Order action successfully redirected to the Checkout Page

        try:
            self.page.wait_for_url("**/checkout/**", timeout=15000)
            print(f"Successfully initiated Pre-Order for: \n\n'{clean_first_item}'")

        except Exception:
            raise AssertionError(f"Timed out waiting for checkout page. Current URL: {self.page.url}")

