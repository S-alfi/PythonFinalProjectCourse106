

class LoadedPreOrderPage:
    def __init__(self, page):
        print("\n### Pre-order Page ###\n")
        self.page = page


    def loaded_navigate_to_the_pre_order_page(self):

        # Navigate to the pre-order page

        pre_order_btn = self.page.get_by_role("link", name="Pre-Order", exact=True)
        pre_order_btn.click()


    def loaded_click_region_toggle_button(self):

        # Click the region toggle button

        self.page.wait_for_selector('[class="switch-label"]', state="visible", timeout=10000)

        region_toggle_btn = self.page.locator('[class="switch-label"]')
        region_toggle_btn.click()
        self.page.wait_for_timeout(3000)


    def loaded_pre_order_first_item(self):

        # Click on the first item on the pre-order page

        first_item = self.page.locator('div[class="product-info"] a >> visible=true').first
        first_item.scroll_into_view_if_needed()
        clean_first_item = first_item.inner_text().strip()
        first_item.click()

        # Click the pre-order button to be redirected to the checkout page

        pre_order_btn = self.page.locator('#product-buynow-button')
        pre_order_btn.wait_for(state="visible", timeout=10000)
        pre_order_btn.click()

        # Verify that the pre-order action successfully redirected to the checkout page

        current_url = self.page.url
        assert current_url == "https://www.loaded.com/checkout/", "The current page URL is incorrect."

        print(f"Successfully initiated pre-order for: \n\n'{clean_first_item}'")

