from playwright.sync_api import Page

class Shoping_cartpage:

 def __init__(self,page:Page):
    self.page = page
    
    self.cart_empty_msg= page.locator("div[id='content'] p")
    self.product_row = page.locator(
    "#content form .table-responsive tbody tr").first

    self.product_name = self.product_row.locator("td:nth-child(2) > a")
    self.product_price = self.product_row.locator("td:nth-child(5)")
    self.quantity_box= self.product_row.locator('input[name^="quantity["]')
    self.update_icon = self.product_row.locator('button[type="submit"]')
    self.remove_icon = page.locator(".fa.fa-times-circle")
    self.checkout_btn = page.locator(".pull-right .btn.btn-primary")
    



 def quantity(self, quantity):
   self.quantity_box.fill(str(quantity))

 def update_icon_click(self):
   self.update_icon.click()

 def remove_icon_click(self):
   self.remove_icon.click()

 def checkoutbutton(self):
   self.checkout_btn.click()





