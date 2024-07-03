from playwright.sync_api import Page


class Header:

    def __init__(self, page: Page):
        self.page = page

    def open_header(self):
        self.page.goto('https://www.collierscanada.com/en-ca')

    def open_services_dropdown(self):
        self.page.click('//a[@aria-label="Services"]')

    def open_properties_dropdown(self):
        self.page.click('//a[@aria-label="Properties"]')

    def open_research_dropdown(self):
        self.page.click('//a[@aria-label="Research"]')

    def open_about_us_dropdown(self):
        self.page.click('//a[@aria-label="About Us"]')

    def open_insights_and_news_dropdown(self):
        self.page.click('//a[@aria-label="Insights & News"]')

    def open_region_dropdown(self):
        self.page.click()