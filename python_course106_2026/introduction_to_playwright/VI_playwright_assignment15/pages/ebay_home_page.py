

class EbayHomePage:
    def __init__(self, page):
        print("\n### Home Page ###\n")
        self.page = page


    def ebay_search_input_box_fill(self):
        search_input_box = self.page.locator('#gh-ac')
        search_input_box.click()
        search_input_box.fill("Sneakers")

        self.page.keyboard.press("Enter")

