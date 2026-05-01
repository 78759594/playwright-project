import time

import playwright
from playwright.sync_api import Page, Playwright, expect, sync_playwright


def test_login_web(page : Page ):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        page.get_by_label("Username:").fill("rahulshettyacademy")
        page.get_by_label("Password:").fill("Learning@830$3mK2")
        page.locators("#terms").click()
        page.get_by_role("button", name = "sign in").click()

