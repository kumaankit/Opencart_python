import pytest
from playwright.sync_api import expect
from pages.home_page import Home_Page
from pages.Login_page import Login_page
from pages.Myaccount_page import Myaccountpage
from pages.Forgetpassword_page import forgetpasswordpage
from utilities.data_reader_util import read_excel_data


login_excel_data = read_excel_data(
    "testdata/logindata.xlsx", "Login_Data"
)


valid_login_data = [
    row[:3] for row in login_excel_data if row[3] == "valid"
]

invalid_password_data = [
    row[:3] for row in login_excel_data if row[3] == "invalid_password"
]

unregistered_email_data = [
    row[:3] for row in login_excel_data if row[3] == "unregistered_email"
]

empty_credentials_data = [
   row[:3] for row in login_excel_data if row[3] == "empty_credentials"
]


@pytest.mark.parametrize("testName,email,password", valid_login_data)
def test_login_with_valid_credentials(page,testName, email,password):
    homepage= Home_Page(page)
    Loginpage = Login_page(page)
    Myaccount = Myaccountpage(page)

    homepage.click_myaccount()
    homepage.click_Login()
    Loginpage.email_text(email)
    Loginpage.pass_text(password)
    Loginpage.login_click()
    expect(Myaccount.text_myaccount).to_be_visible()


@pytest.mark.parametrize("testName, email,password", invalid_password_data)
def test_login_with_invalid_password(page,testName, email,password):
    homepage= Home_Page(page)
    Loginpage = Login_page(page)
    Myaccount = Myaccountpage(page)
    
    homepage.click_myaccount()
    homepage.click_Login()
    Loginpage.email_text(email)
    Loginpage.pass_text(password)
    Loginpage.login_click()
    expect(Loginpage.loginerror_msg).to_be_visible()

@pytest.mark.parametrize("testName, email,password", unregistered_email_data )
def test_login_with_unregistered_email(page,testName, email,password):
    homepage= Home_Page(page)
    Loginpage = Login_page(page)
    Myaccount = Myaccountpage(page)
        
    homepage.click_myaccount()
    homepage.click_Login()
    Loginpage.email_text(email)
    Loginpage.pass_text(password)
    Loginpage.login_click()
    expect(Loginpage.loginerror_msg).to_be_visible()


@pytest.mark.parametrize("testName, email,password", empty_credentials_data )
def test_login_with_empty_credentials(page,testName, email,password):
    homepage= Home_Page(page)
    Loginpage = Login_page(page)
    Myaccount = Myaccountpage(page)
        
    homepage.click_myaccount()
    homepage.click_Login()
    Loginpage.login_click()
    expect(Loginpage.loginerror_msg).to_be_visible()


def test_navigate_to_forgot_password_page(page):
    homepage= Home_Page(page)
    Loginpage = Login_page(page)
    Myaccount = Myaccountpage(page)
    Forgetpass = forgetpasswordpage(page)

        
    homepage.click_myaccount()
    homepage.click_Login()
    Loginpage.forget_link()

    expect(Forgetpass.forgettext_heading).to_be_visible()










    





    


    
    



   



