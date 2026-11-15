from playwright.sync_api import Page

class forgetpasswordpage:
    def __init__(self, page:Page):
        self.page= page
        self.forgettext_heading = page.get_by_role("heading", name="Forgot Your Password?")
    