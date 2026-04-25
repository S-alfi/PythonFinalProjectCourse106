

class LoadedLatestGamesPage:
    def __init__(self, page):
        print("\n### Latest Games Page ###\n")
        self.page = page


    def loaded_navigate_to_the_latest_games_page(self):

        # Navigate to the latest games page

        latest_games_btn = self.page.get_by_role("link", name="Latest Games")
        latest_games_btn.click()

        # Validate that the loaded page URL matches the expected latest games page

        current_url = self.page.url
        assert "latest-games" in current_url, f"Expected 'latest-games' in {current_url}"


    def loaded_click_region_toggle_button(self):

        # Click the region toggle button

        self.page.wait_for_selector('[class="switch-label"]', state="visible", timeout=10000)

        region_toggle_btn = self.page.locator('[class="switch-label"]')
        region_toggle_btn.click()
        self.page.wait_for_timeout(3000)


    # The loaded_sort_top_5_games function: Extracts the first five unique game franchises from a visible product list and prints their titles and prices.

    def loaded_sort_top_5_games(self):

        latest_games_top_5_games_list = []
        seen_core_names = set()

        self.page.wait_for_selector('div[class="product-info"]', state="visible", timeout=10000)

        products = self.page.query_selector_all('div[class="product-info"]')

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

        print("Top 5 games:\n")

        for index, game in enumerate(latest_games_top_5_games_list, start=1):
            print(f"{index}. {game}")

