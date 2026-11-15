from playwright.sync_api import Page

class ProductdetailPage:

 def __init__(self,page:Page):
    self.page = page
    
    self.product_title= page.locator("[class= 'col-sm-4'] h1")
    self.product_price = page.locator("[class= 'list-unstyled'] h2")
    self.prouctpage_img = page.locator(".thumbnail img").nth(0)
    self.productpage_description= page.locator("#tab-description")
    self.add_to_Cart_btn = page.locator("#button-cart")
    self.success_addproduct_msg = page.locator(".alert-success")
    self.quantityaddproduct= page.locator("#input-quantity")
    self.checkout_page= page.locator('.alert-success a[href*="route=checkout/cart"]')
    self.cart_icon = page.locator("#cart-total")
    self.cancel_product = page.locator(".btn.btn-danger.btn-xs")
            
   

 def cart_button(self):
   self.add_to_Cart_btn.click()

 def add_quantity(self, quantity):
   self.quantityaddproduct.fill(str(quantity))

 def checkout_btn(self):
   self.checkout_page.click()

 def product_name_and_price(self):
   Capture_name= self.product_title.inner_text().strip()
   Capture_price = self.product_price.inner_text().strip()
   return Capture_name , Capture_price

 def remove_cart(self):
   self.cart_icon.click()
   self.cancel_product.click()
         

 
   
   
   
   
   






   
   

