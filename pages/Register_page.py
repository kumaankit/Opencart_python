from playwright.sync_api import Page

class RegisterPage:

 def __init__(self,page:Page):
    self.page = page

    self.heading = page.locator("[class = 'col-sm-9'  ] h1")
    self.firstName= page.get_by_placeholder("First Name")
    self.lastName= page.get_by_placeholder("Last Name")
    self.email= page.get_by_placeholder("E-Mail")
    self.telephoneno= page.get_by_placeholder("Telephone")
    self.password = page.get_by_placeholder("Password" , exact=True)
    self.confirmpassword= page.get_by_placeholder("Password Confirm")
    self.subscribe_btn = page.get_by_label("Yes")
    self.chkbox= page.locator('[name="agree"]')
    self.btn= page.locator(".btn.btn-primary")
    self.heading2= page.get_by_text("Your Account Has Been Created!")
    self.register_error_msg= page.locator(".alert-danger")
    self.register_confirm_password_not_match = page.locator(".text-danger")



 def  set_firstName (self , fname):
    self.firstName.fill(fname)
 def set_lastName(self,Lname):
    self.lastName.fill(Lname)
 def set_Email(self, Email):
    self.email.fill(Email)
 def set_PhoneNo(self,PhoenNo):
    self.telephoneno.fill(str(PhoenNo))

 def set_password(self, Pass):
    self.password.fill(Pass)
 def set_confpassword(self, confpass):
    self.confirmpassword.fill(confpass)

 def subscribe_button(self ):
    self.subscribe_btn.click()
    

 def checkbox(self):
    self.chkbox.check()
 def btn_click(self):
    self.btn.click()

 
    

 
    
    
 
