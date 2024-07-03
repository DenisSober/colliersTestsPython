from playwright.sync_api import Page, expect
from pages.header import Header


def test_header_dropdowns_opening(page: Page):
    header = Header(page)
    header.open_header()
    expect(page).to_have_url('https://www.collierscanada.com/en-ca')
    header.open_services_dropdown()
    expect(page.locator('//a[@aria-label="Optimize Property Performance"]')).to_be_visible()
    header.open_properties_dropdown()
    expect(page.locator('//a[contains(text(), "Search Properties")]')).to_be_visible()
    header.open_research_dropdown()
    expect(page.locator('//a[contains(text(), "Research Types")]')).to_be_visible()
    header.open_about_us_dropdown()
    expect(page.locator('//a[contains(text(), "Sustainability")]')).to_be_visible()
    header.open_insights_and_news_dropdown()
    expect(page.locator('//a[contains(text(), "Podcast")]')).to_be_visible()
