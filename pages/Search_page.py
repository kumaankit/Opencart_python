from playwright.sync_api import Page

class SearchPage:
    def __init__(self, page:Page):
        self.page= page
        
        self.No_product_msg = page.get_by_text("There is no product that matches the search criteria.", exact=True)
        self.products_title = page.locator(".caption a")
        self.product_prices = page.locator(".caption .price")
        self.product_images = page.locator(".image img")
        self.product_descriptions = page.locator(".product-thumb p:not(.price)")
        self.add_t0_cart= page.locator("span:has-text('ADD TO CART')")
        self.success_addtocart_msg = page.locator(".alert-success")
        
        


    
    def  unrelated_products(self, product_name):
        unrelated = []
        for name in self.products_title.all_text_contents():
            if product_name.casefold() not in name.casefold():
                unrelated.append(name)


        return unrelated

    def select_product_title(self):
        first_product =self.products_title.nth(0)
        first_price =self.product_prices.nth(0)

        capture_name = first_product.inner_text().strip()
        captured_price =first_price.inner_text().splitlines()[0].strip()
        first_product.click()
        return capture_name, captured_price

    def product_image(self):
        self.product_images.nth(0).click()

    def product_description(self):
        first_description = self.product_descriptions.nth(0)
        capture_description= first_description.inner_text().strip().rstrip(".").strip()
        first_product =self.products_title.nth(0)
        first_product.click()
        return capture_description

    def addtocart_click(self):
        self.add_t0_cart.nth(0).click()

   

    

        
      
       



   







