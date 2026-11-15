
import pytest
from playwright.sync_api import expect
from pages.Login_page import Login_page
from pages.home_page import Home_Page
from pages.Myaccount_page import Myaccountpage
from pages.Search_page import SearchPage
from pages.Productdetail_page import ProductdetailPage
from utilities.data_reader_util import read_excel_data
from pages.Checkout_page import checkoutpage
from pages.Shoppingcart_page import Shoping_cartpage


login_excel_data = read_excel_data("testdata/logindata.xlsx" , "Login_Data")
product_excel_data = read_excel_data("testdata/logindata.xlsx" ,"search_product" )

valid_login_data = [row[:3] for row  in login_excel_data if row[3]== "valid"]

Search_valid_product_name = [row[:2] for row in product_excel_data if row[2] == "valid product name"]

@pytest.mark.parametrize("login_test_name, email, password", valid_login_data)
@pytest.mark.parametrize("product_test_name, product_name" , Search_valid_product_name)
def test_add_product_to_cart_from_product_page(page,login_test_name,email,password, product_test_name,product_name ):
    homepage = Home_Page(page)
    loginPage = Login_page(page)
    myaccountpage = Myaccountpage(page)
    searchpage = SearchPage(page)
    productpage= ProductdetailPage(page)
    

    homepage.click_myaccount()
    homepage.click_Login()
    loginPage.email_text(email)
    loginPage.pass_text(password)
    loginPage.login_click()
    myaccountpage.searchbox(product_name)
    myaccountpage.searchbutton()
    searchpage.select_product_title()
    productpage.cart_button()
    expect(productpage.success_addproduct_msg).to_be_visible()





@pytest.mark.parametrize("login_test_name, email, password", valid_login_data)
@pytest.mark.parametrize("product_test_name, product_name" , Search_valid_product_name)
def test_add_product_to_cart_from_search_results(page,login_test_name,email,password, product_test_name,product_name ):
    homepage = Home_Page(page)
    loginPage = Login_page(page)
    myaccountpage = Myaccountpage(page)
    searchpage = SearchPage(page)
    productpage= ProductdetailPage(page)
    

    homepage.click_myaccount()
    homepage.click_Login()
    loginPage.email_text(email)
    loginPage.pass_text(password)
    loginPage.login_click()
    myaccountpage.searchbox(product_name)
    myaccountpage.searchbutton()
    searchpage.addtocart_click()
    expect(searchpage.success_addtocart_msg).to_be_visible()


@pytest.mark.parametrize("login_test_name, email, password", valid_login_data)
@pytest.mark.parametrize("product_test_name, product_name" , Search_valid_product_name)
def test_add_multiple_quantities_to_cart(page,login_test_name,email,password, product_test_name,product_name ):
    homepage = Home_Page(page)
    loginPage = Login_page(page)
    myaccountpage = Myaccountpage(page)
    searchpage = SearchPage(page)
    productpage= ProductdetailPage(page)
    

    homepage.click_myaccount()
    homepage.click_Login()
    loginPage.email_text(email)
    loginPage.pass_text(password)
    loginPage.login_click()
    myaccountpage.searchbox(product_name)
    myaccountpage.searchbutton()
    searchpage.select_product_title()

    productpage.add_quantity(2)
    expect(productpage.quantityaddproduct).to_have_value("2")
    productpage.cart_button()

@pytest.mark.parametrize("login_test_name, email, password", valid_login_data)
@pytest.mark.parametrize("product_test_name, product_name" , Search_valid_product_name)
def test_add_product_with_invalid_quantity(page,login_test_name,email,password, product_test_name,product_name ):
    homepage = Home_Page(page)
    loginPage = Login_page(page)
    myaccountpage = Myaccountpage(page)
    searchpage = SearchPage(page)
    productpage= ProductdetailPage(page)
    Shoppingcart_page = Shoping_cartpage(page)
    

    homepage.click_myaccount()
    homepage.click_Login()
    loginPage.email_text(email)
    loginPage.pass_text(password)
    loginPage.login_click()
    myaccountpage.searchbox(product_name)
    myaccountpage.searchbutton()
    searchpage.select_product_title()
    productpage.remove_cart()
   
    productpage.add_quantity(0)
    
    productpage.cart_button()
    
    homepage.click_shopping_cart()
    
    expect(Shoppingcart_page.cart_empty_msg).to_have_text(
    "Your shopping cart is empty!"
)



    

    
    





    


