import time

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

        # mouse hover action
        #page.goto("https://rahulshettyacademy.com/AutomationPractice/")
        page.locator("#mousehover").hover()
        page.get_by_role("link",name="Top").click()
        time.sleep(2)



        # alert handle
        page.on("dialog",lambda dialog:dialog.accept())
        page.get_by_role("button",name="Confirm").click()


        # frame handling
        pageFrame = page.frame_locator("#courses-iframe")
        pageFrame.get_by_role("link", name="All Access plan").click()
        expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")

        # check price of rice is equal to 30 from table
        page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
        for index in range(page.locator("th").count()):
            if page.locator("th").nth(index).filter(has_text="Price").count()>0:
                colValue = index
                print(f"price col value is {colValue}")
                break

        riceRow = page.locator("tr").filter(has_text="Rice")
        expect(riceRow.locator("td").nth(colValue)).to_have_text("37")


