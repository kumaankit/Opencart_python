import pytest
from playwright.sync_api import expect
from pages.Login_page import Login_page
from pages.home_page import Home_Page
from pages.Myaccount_page import Myaccountpage
from pages.Search_page import SearchPage
from pages.Productdetail_page import ProductdetailPage
from utilities.data_reader_util import read_excel_data

login_excel_data = read_excel_data("testdata/logindata.xlsx" , "Login_Data")
product_excel_data = read_excel_data("testdata/logindata.xlsx" ,"search_product" )

valid_login_data = [row[:3] for row  in login_excel_data if row[3]== "valid"]

Search_valid_product_name = [row[:2] for row in product_excel_data if row[2] == "valid product name"]
@pytest.mark.parametrize("login_test_name, email, password", valid_login_data)
@pytest.mark.parametrize("product_test_name, product_name" , Search_valid_product_name)
def test_verify_product_name_and_price(page,login_test_name,email,password, product_test_name,product_name ):
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
    Capture_name , captured_price = searchpage.select_product_title()
    expect(productpage.product_title).to_have_text(Capture_name)
    expect(productpage.product_price).to_have_text(captured_price)


@pytest.mark.parametrize("login_test_name, email, password", valid_login_data)
@pytest.mark.parametrize("product_test_name, product_name" , Search_valid_product_name)
def test_verify_product_images(page,login_test_name,email,password, product_test_name,product_name ):
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
    searchpage.product_image()
    expect(productpage.prouctpage_img).to_be_visible()

    expect(productpage.prouctpage_img).to_have_js_property(
    "complete", True)

    expect(productpage.prouctpage_img).not_to_have_js_property(
    "naturalWidth", 0)
    

@pytest.mark.parametrize("login_test_name, email, password", valid_login_data)
@pytest.mark.parametrize("product_test_name, product_name" , Search_valid_product_name)
def test_verify_product_description(page,login_test_name,email,password, product_test_name,product_name ):
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
    capture_description = searchpage.product_description()
    expect(productpage.productpage_description).to_contain_text(capture_description)











