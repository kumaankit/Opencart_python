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




@pytest.mark.parametrize("testName,email,password", valid_login_data)
def test_logout_successfully(page,testName, email,password):
    homepage= Home_Page(page)
    Loginpage = Login_page(page)
    Myaccount = Myaccountpage(page)

    homepage.click_myaccount()
    homepage.click_Login()
    Loginpage.email_text(email)
    Loginpage.pass_text(password)
    Loginpage.login_click()
    expect(Myaccount.text_myaccount).to_be_visible()
    homepage.click_myaccount()
    Myaccount.logout_btn()
    expect(Myaccount.success_logout_text).to_be_visible()


@pytest.mark.parametrize("testName,email,password", valid_login_data)
def test_verify_session_after_logout(page,testName, email,password):
    homepage= Home_Page(page)
    Loginpage = Login_page(page)
    Myaccount = Myaccountpage(page)

    homepage.click_myaccount()
    homepage.click_Login()
    Loginpage.email_text(email)
    Loginpage.pass_text(password)
    Loginpage.login_click()
    expect(Myaccount.text_myaccount).to_be_visible()
    account_url = page.url
    homepage.click_myaccount()
    Myaccount.logout_btn()
    expect(Myaccount.success_logout_text).to_be_visible()
    page.go_back()
    page.goto(account_url)
    expect(Loginpage.Email).to_be_visible()
    expect(Loginpage.password).to_be_visible()
    expect(Loginpage.login).to_be_visible()
    expect(Myaccount.text_myaccount).not_to_be_visible()
    




   