import time

from playwright.sync_api import Page, Playwright, expect

def test_login_web(page : Page ):
    browser = page.chromium.launch()
    context = browser.new_context()
    page = context.new_page

    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.locators("#terms").click()
    page.get_by_role("button", name = "sign in").click()

