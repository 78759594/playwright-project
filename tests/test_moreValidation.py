from playwright.sync_api import sync_playwright, expect


def test_diff_function():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://rahulshettyacademy.com/AutomationPractice/")

        # to check hidden text and visible text with placeholder
        expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
        page.get_by_role("button",name="Hide").click()
        expect(page.get_by_placeholder("Hide/Show example")).to_be_hidden()

        