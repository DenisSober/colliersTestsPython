from playwright.sync_api import Page

class SearchPage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_page(self):
        self.page.goto('https://www.collierscanada.com/en-ca/search#sort=relevancy')

    def enter_key_word(self, key_word):
        self.page.fill('//input[@placeholder="Keywords"]', key_word)

    def click_search_button(self):
        self.page.click('//*[@id="keywords"]/a')

    def open_first_result_card(self):
        self.page.click('//div[@class="coveo-result-list-container coveo-list-layout-container"]/div[1]/div/div/div[2]/div/h2/a')
