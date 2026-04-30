import time

from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://playwright.dev/")
        title = page.title()
        assert "Playwright" in title
        print(title)
        time.sleep(5)
        browser.close()
