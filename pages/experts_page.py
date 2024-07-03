from playwright.sync_api import Page

class ExpertsPage:
    def __init__(self, page: Page):
        self.page = page

    def click_property_type_arrow(self):
        self.page.locator('//*[@id="PropertyType"]/div[1]/div[1]/div[3]/span').click()

