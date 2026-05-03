from playwright.sync_api import sync_playwright, expect



with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as new_pageinfo:
        page.get_by_text("Free Access to InterviewQues/ResumeAssistance/Material").click()
        childPage = new_pageinfo.value
        text = childPage.locator(".red").text.content()
        print(text)
        words = text.split("at")
        email = words[1].split(" ")[1]
        print(email)
        assert email == "mentor@rahulshettyacademy.com"
        