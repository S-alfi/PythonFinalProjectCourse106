

class EbayAdvancedSearchPage:
    def __init__(self, page):
        print("\n### Advanced Search Page ###\n")
        self.page = page


    def ebay_advanced_button_click(self):

        advanced_btn = self.page.get_by_role("link", name="Advanced")
        advanced_btn.click()

        current_url = self.page.url
        assert current_url == "https://www.ebay.com/sch/ebayadvsearch", "The current page URL is incorrect."


    def ebay_search_for_something_within_the_advanced_search_page(self):

        enter_value_input_box = self.page.locator('label[for="_nkw"][class*="floating-label__label"]')
        enter_value_input_box.clear()
        enter_value_input_box.fill("Hot Wheels")

        self.page.keyboard.press("Enter")

