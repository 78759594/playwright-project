import time

from playwright.sync_api import sync_playwright

def test_login_web(playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page

    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.locators("#terms").click()
    page.get_by_role("button", name = "Sign In").click()

