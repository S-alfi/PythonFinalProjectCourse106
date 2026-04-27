

class LoadedHelpCenterPage:
    def __init__(self, page):
        print("\n### Help Center Page ###\n")
        self.page = page


    def navigate_to_help_center_page(self):

        # Navigate to the Help Center page

        help_center_btn = self.page.get_by_role("link", name="Help Center", exact=True)
        help_center_btn.click()

        # Validate that the Loaded page URL matches the expected Help Center page

        help_center_page_url = self.page.url
        assert "hc" in help_center_page_url, f"Expected 'hc' in {help_center_page_url}"


    def search_for_legal_documents(self):

        # Enter 'Where can I read your Terms & Conditions and Privacy Policy?' into the search input box and press the Enter key

        help_center_search_input_box = self.page.locator('#query')
        help_center_search_input_box.clear()
        help_center_search_input_box.press_sequentially("Where can I read your Terms & Conditions and Privacy Policy?", delay=100)
        self.page.keyboard.press("Enter")

        # Select the first article title from the search results list

        first_result = self.page.locator('[class="search-result-title"]').first
        first_result.wait_for(state="visible", timeout=10000)
        assert first_result.count() > 0, "No search results were found for the legal documents query."
        first_result.click()

        # Extract the Privacy Policy and Terms & Conditions links from the article body

        legal_info_node = self.page.query_selector_all('[class="wysiwyg-underline"]')
        privacy_policy_link = legal_info_node[0].inner_text()
        terms_conditions_link = legal_info_node[1].inner_text()

        print(F"Privacy Policy: {privacy_policy_link}\nTerms & Conditions: {terms_conditions_link}")

