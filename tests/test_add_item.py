from playwright.sync_api import sync_playwright, expect


def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        page.get_by_label("Username").fill("rahulshettyacademy")
        page.get_by_label("Password").fill("Learning@830$3mK2")
        teacher = page.get_by_role("combobox").select_option("Teacher")
        print(teacher)
        page.get_by_role("link", name ="terms and conditions").click()
        page.get_by_role("button", name="sign in").click()

        title = page.title()
        assert "LoginPage Practise | Rahul Shetty Academy" in title

        iphone = page.locator("app-card").filter(has_text="iphone X")
        iphone.get_by_role("button").click()
        nokia=page.locator("app-card").filter(has_text="Nokia Edge")
        nokia.get_by_role("button").click()

        page.get_by_text("Checkout").click()

        expect(page.locator(".media-body")).to_have_count(2)