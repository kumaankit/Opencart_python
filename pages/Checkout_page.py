from playwright.sync_api import Page

class checkoutpage:
    def __init__(self, page:Page):
        self.page = page

        
        self.first_name = page.get_by_placeholder("First Name")
        self.Last_name = page.get_by_placeholder("Last Name")
        self.Company = page.get_by_placeholder("Company")
        self.Address = page.get_by_placeholder("Address 1")
        self.city = page.get_by_placeholder("City")
        self.Post_code = page.get_by_placeholder("Post Code")
        self.country = page.locator("#input-payment-country")
        self.State = page.locator("#input-payment-zone")

        
        self.continue_btn= page.locator("#button-payment-address")
        self.deliverycontinuebtn= page.locator("#button-shipping-address")
        self.ratecontinuebtn= page.locator("#button-shipping-method")
        self.agreechekcbox = page.locator("[name='agree']")
        self.cashondeliverycontinuebtn = page.locator("#button-payment-method")
        self.confirorderbtn = page.locator("#button-confirm")
        self.orderplacemsg = page.get_by_role("heading", name="Your order has been placed!")
        self.New_address= page.get_by_label("I want to use a new address")
        self.guest_btn= page.locator("[value='guest']")
        self.guest_Continue_button = page.locator("#button-account")
        self.email_box= page.locator("#input-payment-email")
        self.telephone_boxs= page.locator("#input-payment-telephone")
        self.billing_detail_continue_btn= page.locator("#button-guest")
        self.guest_delivery_continuebtn= page.locator("#button-shipping-method")
        self.term_checkbox= page.locator("[name='agree']")
        self.guest_error_msg= page.get_by_text("First Name must be between 1 and 32 characters!")
        self.shipping= page.locator("[name='shipping_method']")
        self.payment= page.locator("[name='payment_method']")

      
        
        

    def set_First_Name(self, fname):
        self.first_name.fill(fname)

    def set_last_name(self, Lname):
        self.Last_name.fill(Lname)

    def set_companyName(self, compName):
        self.Company.fill(compName)

    def set_AddressName(self,Address):
        self.Address.fill(Address)

    def set_CityName(self,City):
        self.city.fill(City)

    def set_postalcode(self,postal):
        self.Post_code.fill(str(postal))

    def set_coutryName(self, country):
        self.country.select_option(label=country)

    def  set_stateName(self, state):
        self.State.select_option(label=state)

    def  continuebutton(self):
        self.continue_btn.click()

    def deliverycontinuebutton(self):
        self.deliverycontinuebtn.click()

    def ratecontinuebutton(self):
        self.ratecontinuebtn.click()

    def agreechk_box(self):
        self.agreechekcbox.check()

    def cashondeliverycontinue_button(self):
        self.cashondeliverycontinuebtn.click()

    def confirorderbutton(self):
        self.confirorderbtn.click()

    def new_address(self):
        self.New_address.click()

    def guest_button(self):
        self.guest_btn.check()

    def guest_continue_button(self):
        self.guest_Continue_button.click()

    def Email_box(self, email):
        self.email_box.fill(email)

    def telephone_box(self, telephone):
        self.telephone_boxs.fill(str(telephone))

    def billing_continue_button(self):
        self.billing_detail_continue_btn.click()

    def guest_delivery_btn(self):
         self.guest_delivery_continuebtn.click()

    def term_chkbox(self):
        self.term_checkbox.click()

  




    
    
        


 



    



    




    