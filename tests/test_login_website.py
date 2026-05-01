import time

import playwright
from playwright.sync_api import Page, Playwright, expect, sync_playwright


def test_login_web():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        #login test case
        page.get_by_label("Username:").fill("rahulshettyacademy")
        page.get_by_label("Password:").fill("Learning")
        # select checkbox
        page.locator("#terms").check()
        # to click link
        page.get_by_role("link", name ="terms and conditions").click()
        # select drop down
        teacher = page.get_by_role("combobox").select_option("Teacher")
        print(teacher)
        page.get_by_role("button", name = "sign in").click()
        # to validate assertion with test case
        expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        page.get_by_label("Username").fill("rahulshettyacademy")
        page.get_by_label("Password").fill("Learning@830$3mK2")
        page.get_by_role("radio", name="Student").check()
        page.get_by_label("I Agree to the terms and conditions").check()
        page.get_by_role("button", name="Sign In").click()

        title = page.title()
        assert "ProtoCommerce" in title
        #assert page.is_visible("text=Welcome")

def test_diff_function():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://rahulshettyacademy.com/AutomationPractice/")






