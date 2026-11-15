from playwright.sync_api import Page

class Login_page:
   def __init__(self , page:Page):
     self.page = page

     self.Email= page.get_by_placeholder("E-Mail Address")
     self.password = page.get_by_placeholder("Password")
     self.forgetlink= page.locator("[class='form-group'] a")
     self.login = page.get_by_role("button", name="Login")
     self.loginerror_msg = page.locator(".alert-danger")
     
     


   def  email_text(self, mail):
     self.Email.fill(mail)
     

   def pass_text(self, Pass):
     self.password.fill(Pass)

   def login_click(self):
     self.login.click()

   def forget_link(self):
     self.forgetlink.click()

  

     
     
     


