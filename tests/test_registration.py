import pytest

from pages.home_page import Home_Page
from pages.Register_page import RegisterPage
from playwright.sync_api import  expect
from utilities.data_reader_util import read_excel_data

Register_excel_data = read_excel_data(
    "testdata/logindata.xlsx", "Register_Data")

register_mandatory_fields = [row[:7] for row in Register_excel_data if row[7] == "valid_mandatory_fields"]
register_all_fields = [row[:7] for row in Register_excel_data if row[7] == "valid_all_fields"]
register_existing_email = [row[:7] for row in Register_excel_data if row[7] == "existing_email"]
register_mismatched_passwords = [row[:7] for row in Register_excel_data if row[7] == "mismatched_passwords"]
register_without_privacy_policy = [row[:7] for row in Register_excel_data if row[7] == "without_privacy_policy"]







@pytest.mark.parametrize("testName,first_name,Last_name, Email, Telephone, Password,Password_confirm", register_mandatory_fields)
def test_register_with_mandatory_fields(page, testName,first_name,Last_name, Email, Telephone, Password,Password_confirm):
    homepage= Home_Page(page)
    register_page = RegisterPage(page)
    homepage.click_myaccount()
    homepage.click_Registerclick()
    expect(register_page.heading).to_be_visible()
    register_page.set_firstName(first_name)
    register_page.set_lastName(Last_name)
    register_page.set_Email(Email)
    register_page.set_PhoneNo(Telephone)
    register_page.set_password(Password)
    register_page.set_confpassword(Password_confirm)
    register_page.checkbox()
    register_page.btn_click()
    expect(register_page.heading2).to_be_visible()

@pytest.mark.parametrize("testName,first_name,Last_name, Email, Telephone, Password,Password_confirm", register_all_fields )
def test_register_with_all_fields(page, testName,first_name,Last_name, Email, Telephone, Password,Password_confirm):
    homepage= Home_Page(page)
    register_page = RegisterPage(page)
    homepage.click_myaccount()
    homepage.click_Registerclick()
    expect(register_page.heading).to_be_visible()
    register_page.set_firstName(first_name)
    register_page.set_lastName(Last_name)
    register_page.set_Email(Email)
    register_page.set_PhoneNo(Telephone)
    register_page.set_password(Password)
    register_page.set_confpassword(Password_confirm)
    register_page.subscribe_button()
    register_page.checkbox()
    register_page.btn_click()
    expect(register_page.heading2).to_be_visible()


@pytest.mark.parametrize("testName,first_name,Last_name, Email, Telephone, Password,Password_confirm", register_existing_email)
def test_register_with_existing_email(page, testName,first_name,Last_name, Email, Telephone, Password,Password_confirm):
    homepage= Home_Page(page)
    register_page = RegisterPage(page)
    homepage.click_myaccount()
    homepage.click_Registerclick()
    expect(register_page.heading).to_be_visible()
    register_page.set_firstName(first_name)
    register_page.set_lastName(Last_name)
    register_page.set_Email(Email)
    register_page.set_PhoneNo(Telephone)
    register_page.set_password(Password)
    register_page.set_confpassword(Password_confirm)
    register_page.checkbox()
    register_page.btn_click()
    expect(register_page.register_error_msg).to_be_visible()


@pytest.mark.parametrize("testName,first_name,Last_name, Email, Telephone, Password,Password_confirm", register_mismatched_passwords)
def test_register_with_mismatched_passwords(page, testName,first_name,Last_name, Email, Telephone, Password,Password_confirm):
    homepage= Home_Page(page)
    register_page = RegisterPage(page)
    homepage.click_myaccount()
    homepage.click_Registerclick()
    expect(register_page.heading).to_be_visible()
    register_page.set_firstName(first_name)
    register_page.set_lastName(Last_name)
    register_page.set_Email(Email)
    register_page.set_PhoneNo(Telephone)
    register_page.set_password(Password)
    register_page.set_confpassword(Password_confirm)
    register_page.checkbox()
    register_page.btn_click()
    expect(register_page.register_confirm_password_not_match).to_be_visible()


@pytest.mark.parametrize("testName,first_name,Last_name, Email, Telephone, Password,Password_confirm", register_without_privacy_policy)
def test_register_without_privacy_policy(page, testName,first_name,Last_name, Email, Telephone, Password,Password_confirm):
    homepage= Home_Page(page)
    register_page = RegisterPage(page)
    homepage.click_myaccount()
    homepage.click_Registerclick()
    expect(register_page.heading).to_be_visible()
    register_page.set_firstName(first_name)
    register_page.set_lastName(Last_name)
    register_page.set_Email(Email)
    register_page.set_PhoneNo(Telephone)
    register_page.set_password(Password)
    register_page.set_confpassword(Password_confirm)
    register_page.btn_click()
    expect(register_page.register_error_msg).to_contain_text("Warning: You must agree to the Privacy Policy!")




















    


    
    
    


    
    
   
 
    




    









   