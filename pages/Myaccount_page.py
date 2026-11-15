from playwright.sync_api import Page

class Myaccountpage:
    def __init__(self, page:Page):
        self.page= page
        self.text_myaccount = page.locator("h2:has-text('My Account')")
        self.seachbox= page.get_by_placeholder("Search")
        self.searchbtn= page.locator("#search button .fa-search")
        self.logout= page.locator("#column-right").get_by_role("link", name="Logout")
        self.logout_dropdown = page.locator('#top-links .dropdown-menu a[href*="route=account/logout"]')
        self.success_logout_text= page.locator("h1:has-text('Account Logout')")


    def searchbox(self, product):
        self.seachbox.fill(product)
    def searchbutton(self):
        self.searchbtn.click()
    def logout_link(self):
        self.logout.click()
    def logout_btn(self):
        self.logout_dropdown.click()


