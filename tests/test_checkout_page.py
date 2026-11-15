import pytest
from playwright.sync_api import expect
from pages.Login_page import Login_page
from pages.home_page import Home_Page
from pages.Myaccount_page import Myaccountpage
from pages.Search_page import SearchPage
from pages.Productdetail_page import ProductdetailPage
from pages.Shoppingcart_page import Shoping_cartpage
from utilities.data_reader_util import read_excel_data
from pages.Checkout_page import checkoutpage
from pages.Register_page import RegisterPage

login_excel_data = read_excel_data("testdata/logindata.xlsx" , "Login_Data")
checkout_excel_data= read_excel_data("testdata/logindata.xlsx" ,"Checkout" )



valid_login_data = [row[:3] for row  in login_excel_data if row[3]== "valid"]
Checkout_registered_user= [row[:8] for row in checkout_excel_data if row[8] == "registered_user"]


@pytest.mark.parametrize("login_test_name, email, password", valid_login_data)
@pytest.mark.parametrize("checkout_billingdetail_test_name,product, First_name, Last_name, Company, Address, City, Post_Code", Checkout_registered_user)
def test_checkout_as_registered_user(page,login_test_name,email,password , checkout_billingdetail_test_name,product,  First_name, Last_name, Company, Address, City, Post_Code):
    homepage = Home_Page(page)
    loginPage = Login_page(page)
    myaccountpage = Myaccountpage(page)
    searchpage = SearchPage(page)
    productpage= ProductdetailPage(page)
    shopping_cart = Shoping_cartpage(page)
    checkout_page = checkoutpage(page)
    
    homepage.click_myaccount()
    homepage.click_Login()
    loginPage.email_text(email)
    loginPage.pass_text(password)
    loginPage.login_click()
    myaccountpage.searchbox(product)
    myaccountpage.searchbutton()
    searchpage.select_product_title()
    productpage.remove_cart()
    productpage.cart_button()
    productpage.checkout_btn()
    shopping_cart.checkoutbutton()
    checkout_page.new_address()
    checkout_page.set_First_Name(First_name)
    checkout_page.set_last_name(Last_name)
    checkout_page.set_companyName(Company)
    checkout_page.set_AddressName(Address)
    checkout_page.set_CityName(City)
    checkout_page.set_postalcode(Post_Code)
    checkout_page.set_coutryName("Togo")
    checkout_page.set_stateName("Kara")
    checkout_page.continuebutton()
    checkout_page.deliverycontinuebutton()
    checkout_page.ratecontinuebutton()
    checkout_page.agreechk_box()
    checkout_page.cashondeliverycontinue_button()
    checkout_page.confirorderbutton()
    expect(checkout_page.orderplacemsg).to_be_visible()




@pytest.mark.parametrize("checkout_billingdetail_test_name, product,First_name, Last_name, Company, Address, City, Post_Code", Checkout_registered_user)
def test_checkout_as_guest_user(page, checkout_billingdetail_test_name, product, First_name, Last_name, Company, Address, City, Post_Code):
    
    myaccountpage = Myaccountpage(page)
    searchpage = SearchPage(page)
    productpage= ProductdetailPage(page)
    shopping_cart = Shoping_cartpage(page)
    checkout_page = checkoutpage(page)
    loginPage = Login_page(page)
    Register_page= RegisterPage(page)

    myaccountpage.searchbox(product)
    myaccountpage.searchbutton()
    searchpage.select_product_title()
    productpage.cart_button()
    productpage.checkout_btn()
    shopping_cart.checkoutbutton()
    checkout_page.guest_button()
    expect(checkout_page.guest_btn).to_be_checked()
    checkout_page.guest_continue_button()
    checkout_page.set_First_Name(First_name)
    checkout_page.set_last_name(Last_name)
    checkout_page.Email_box("ankit123@gmail.com")
    checkout_page.telephone_box("8493872376")
    checkout_page.set_companyName(Company)
    checkout_page.set_AddressName(Address)
    checkout_page.set_CityName(City)
    checkout_page.set_postalcode(Post_Code)
    checkout_page.set_coutryName("Togo")
    checkout_page.set_stateName("Kara")
    checkout_page.billing_continue_button()
    checkout_page.guest_delivery_btn()
    checkout_page.term_chkbox()
    checkout_page.cashondeliverycontinue_button()
    checkout_page.confirorderbutton()
    expect(checkout_page.orderplacemsg).to_be_visible()



@pytest.mark.parametrize("checkout_billingdetail_test_name, product, First_name, Last_name, Company, Address, City, Post_Code", Checkout_registered_user)
def test_checkout_with_empty_billing_details(page , checkout_billingdetail_test_name, product, First_name, Last_name, Company, Address, City, Post_Code):
    
    myaccountpage = Myaccountpage(page)
    searchpage = SearchPage(page)
    productpage= ProductdetailPage(page)
    shopping_cart = Shoping_cartpage(page)
    checkout_page = checkoutpage(page)
    loginPage = Login_page(page)
    Register_page= RegisterPage(page)

    myaccountpage.searchbox(product)
    myaccountpage.searchbutton()
    searchpage.select_product_title()
    productpage.cart_button()
    productpage.checkout_btn()
    shopping_cart.checkoutbutton()
    checkout_page.guest_button()
    expect(checkout_page.guest_btn).to_be_checked()
    checkout_page.guest_continue_button()
    checkout_page.billing_continue_button()
    expect(checkout_page.guest_error_msg).to_be_visible()



@pytest.mark.parametrize("checkout_billingdetail_test_name, product, First_name, Last_name, Company, Address, City, Post_Code", Checkout_registered_user)
def test_select_shipping_and_payment_methods(page , checkout_billingdetail_test_name, product, First_name, Last_name, Company, Address, City, Post_Code):
    
    myaccountpage = Myaccountpage(page)
    searchpage = SearchPage(page)
    productpage= ProductdetailPage(page)
    shopping_cart = Shoping_cartpage(page)
    checkout_page = checkoutpage(page)
    loginPage = Login_page(page)
    Register_page= RegisterPage(page)

    myaccountpage.searchbox(product)
    myaccountpage.searchbutton()
    searchpage.select_product_title()
    productpage.cart_button()
    productpage.checkout_btn()

    shopping_cart.checkoutbutton()
    checkout_page.guest_button()
    expect(checkout_page.guest_btn).to_be_checked()
    checkout_page.guest_continue_button()
    checkout_page.set_First_Name(First_name)
    checkout_page.set_last_name(Last_name)
    checkout_page.Email_box("ankit123@gmail.com")
    checkout_page.telephone_box("8493872376")
    checkout_page.set_companyName(Company)
    checkout_page.set_AddressName(Address)
    checkout_page.set_CityName(City)
    checkout_page.set_postalcode(Post_Code)
    checkout_page.set_coutryName("Togo")
    checkout_page.set_stateName("Kara")
    checkout_page.billing_continue_button()
    expect(checkout_page.shipping).to_be_checked()
    checkout_page.guest_delivery_btn()
    expect(checkout_page.payment).to_be_checked()
    checkout_page.term_chkbox()
    checkout_page.cashondeliverycontinue_button()
    expect(checkout_page.confirorderbtn).to_be_visible()
    expect(checkout_page.confirorderbtn).to_be_enabled()
   
    
    

    
    


























    
    
    