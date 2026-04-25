

class LoadedHelpCenterPage:
    def __init__(self, page):
        print("\n### Help Center Page ###\n")
        self.page = page


    def loaded_navigate_to_the_help_center_page(self):

        # Navigate to the help center page

        pre_order_btn = self.page.get_by_role("link", name="Help Center", exact=True)
        pre_order_btn.click()

        # Validate that the loaded page URL matches the expected help center page

        current_url = self.page.url
        assert "hc" in current_url, f"Expected 'hc' in {current_url}"


    def loaded_help_center_page_search(self):

        # Enter 'Where can I read your Terms & Conditions and Privacy Policy?' into the search input box and click the search button

        help_center_search_input_box = self.page.locator('#query')
        help_center_search_input_box.clear()
        help_center_search_input_box.press_sequentially("Where can I read your Terms & Conditions and Privacy Policy?", delay=100)
        self.page.keyboard.press("Enter")

        # Click the first article title in the search results list

        search_result_link = self.page.locator('[class="search-result-title"]').first
        search_result_link.click()

        legal_document_links = self.page.query_selector_all('[class="wysiwyg-underline"]')
        privacy_policy_link = legal_document_links[0].inner_text()
        terms_conditions_link = legal_document_links[1].inner_text()

        print(F"Privacy Policy: {privacy_policy_link}\nTerms & Conditions: {terms_conditions_link}")

