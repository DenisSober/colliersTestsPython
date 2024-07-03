import json
from playwright.sync_api import Page
from pages.search_page import SearchPage


with (open('C:/Users/randa/PycharmProjects/testsColliers/test_data_fixed/key_words_for_search.json', 'r', encoding='utf8')
      as file):
    data = json.load(file)
    test_key_words = data['key_words']


def test_search_by_key_word(page: Page):
    words = test_key_words
    search_page = SearchPage(page)
    search_page.go_to_page()
    for word in words:
        page.wait_for_selector('//input[@placeholder="Keywords"]')
        search_page.enter_key_word(word)
        search_page.click_search_button()
        first_card_link_locator = search_page.page.locator('//div[@class="coveo-result-list-container coveo-list-layout-container"]/div[1]/div/div/div[2]/div/h2/a')
        first_card_link = first_card_link_locator.get_attribute('href')
        first_card_url = 'https://www.collierscanada.com/' + first_card_link
        page.goto(first_card_url)
        page_content = page.inner_text('html')
        assert word in page_content.lower()
        search_page.go_to_page()

