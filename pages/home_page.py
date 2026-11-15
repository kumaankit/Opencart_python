from playwright.sync_api import Page

class Home_Page:
    def __init__(self, page:Page):
        self.page = page

        self.Myaccount= page.locator(".caret")
        self.register = page.get_by_role("link" ,name ="Register")
        self.login= page.get_by_role("link" , name = "Login")
        self.shopping_cart= page.get_by_text("Shopping Cart", exact=True)

    def click_myaccount(self):
        self.Myaccount.click()
        
        
    def click_Registerclick(self):   
        self.register.click()

    def  click_Login(self):
        self.login.click()

    def click_shopping_cart(self):
        self.shopping_cart.click()

    
