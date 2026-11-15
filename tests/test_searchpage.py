import pytest
from playwright.sync_api import  expect
from pages.home_page import Home_Page
from pages.Login_page import Login_page
from pages.Myaccount_page import Myaccountpage
from pages.Search_page import SearchPage
from utilities.data_reader_util import read_excel_data



login_excel_data = read_excel_data("testdata/logindata.xlsx" ,"Login_Data" )
product_excel_data = read_excel_data("testdata/logindata.xlsx" ,"search_product" )


valid_login_data = [
    row[:3] for row in login_excel_data if row[3] == "valid"]

Search_valid_product_name = [
    row[:2] for row in product_excel_data if row[2] == "valid product name"]
Search_Invalid_product_name =  [
    row[:2] for row in product_excel_data if row[2] == "Invalid product name"]

Search_partial_product_name = [
    row[:2] for row in product_excel_data if row[2] == "partial product name"]

Search_with_empty_keyword = [
    row[:2] for row in product_excel_data if row[2] == "empty keyword"]



@pytest.mark.parametrize("login_test_name, email,password", valid_login_data)
@pytest.mark.parametrize("product_test_name,product_name" , Search_valid_product_name)
def test_search_with_valid_product_name(page,login_test_name, email,password,product_test_name, product_name):
    homepage = Home_Page(page)
    loginPage = Login_page(page)
    myaccountpage = Myaccountpage(page)
    searchpage = SearchPage(page)

    homepage.click_myaccount()
    homepage.click_Login()
    loginPage.email_text(email)
    loginPage.pass_text(password)
    loginPage.login_click()
    myaccountpage.searchbox(product_name)
    myaccountpage.searchbutton()
    expect(searchpage.products_title.first).to_be_visible()
    unrelated = searchpage.unrelated_products(product_name)
    assert unrelated == []

@pytest.mark.parametrize("login_test_name, email,password", valid_login_data)
@pytest.mark.parametrize("product_test_name,product_name" , Search_Invalid_product_name)
def test_search_with_invalid_product_name(page,login_test_name, email,password,product_test_name, product_name):
    homepage = Home_Page(page)
    loginPage = Login_page(page)
    myaccountpage = Myaccountpage(page)
    searchpage = SearchPage(page)

    homepage.click_myaccount()
    homepage.click_Login()
    loginPage.email_text(email)
    loginPage.pass_text(password)
    loginPage.login_click()
    myaccountpage.searchbox(product_name)
    myaccountpage.searchbutton()
    expect(searchpage.No_product_msg).to_be_visible()

@pytest.mark.parametrize("login_test_name, email,password", valid_login_data)
@pytest.mark.parametrize("product_test_name,product_name" , Search_partial_product_name)
def test_search_with_partial_product_name(page,login_test_name, email,password,product_test_name, product_name):
    homepage = Home_Page(page)
    loginPage = Login_page(page)
    myaccountpage = Myaccountpage(page)
    searchpage = SearchPage(page)

    homepage.click_myaccount()
    homepage.click_Login()
    loginPage.email_text(email)
    loginPage.pass_text(password)
    loginPage.login_click()
    myaccountpage.searchbox(product_name)
    myaccountpage.searchbutton()
    expect(searchpage.products_title.first).to_be_visible()
    unrelated = searchpage.unrelated_products(product_name)
    assert unrelated == []



@pytest.mark.parametrize("login_test_name, email,password", valid_login_data)
@pytest.mark.parametrize("product_test_name,product_name" , Search_with_empty_keyword)
def test_search_with_empty_keyword(page,login_test_name, email,password,product_test_name, product_name):
    homepage = Home_Page(page)
    loginPage = Login_page(page)
    myaccountpage = Myaccountpage(page)
    searchpage = SearchPage(page)

    homepage.click_myaccount()
    homepage.click_Login()
    loginPage.email_text(email)
    loginPage.pass_text(password)
    loginPage.login_click()
    myaccountpage.searchbutton()
    expect(searchpage.No_product_msg).to_be_visible()






    







    




