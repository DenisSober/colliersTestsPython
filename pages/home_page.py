from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto('https://www.collierscanada.com/en-ca')


    def open_experts(self):
        self.page.locator('//div[@class="nav-primary__list"]/ul/li[4]').click()

