

class ProductPage:
    def __init__(self, page):
        print("\n### Product Page ###\n")
        self.page = page


    def swag_labs_website_get_price_of_the_first_item(self):
        price_list = self.page.query_selector_all('[class="inventory_item_price"]')
        first_price = price_list[0]
        first_price_inner_text = first_price.inner_text()
        print(f'1. The price of the first item is: {first_price_inner_text}\n')


    def swag_labs_website_set_drop_down_menu(self):
        drop_down_menu = self.page.locator('[class="product_sort_container"]')
        drop_down_menu.select_option(index=2)

