from playwright.sync_api import sync_playwright
import requests  # external library to call OTP API

def fetch_mock_otp(user_id: str) -> str:
    """
    Simulate fetching OTP from an external service.
    In real-world, this could be Twilio, Gmail API, or a custom endpoint.
    """
    # Example mock API endpoint (replace with real one in practice)
    response = requests.get(f"https://mock-otp-service.com/get-otp?user={user_id}")
    if response.status_code == 200:
        otp_code = response.json().get("otp")
        return otp_code
    else:
        raise Exception("Failed to fetch OTP")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Step 1: Navigate to login page
    page.goto("https://example.com/login")

    # Step 2: Enter username & password
    page.fill("input[name='username']", "testuser")
    page.fill("input[name='password']", "password123")
    page.click("text=Login")

    # Step 3: Wait for OTP input field
    page.wait_for_selector("input[name='otp']")

    # Step 4: Fetch OTP from external service
    otp_code = fetch_mock_otp("testuser")
    print(f"Fetched OTP: {otp_code}")

    # Step 5: Enter OTP and verify
    page.fill("input[name='otp']", otp_code)
    page.click("text=Verify")

    # Step 6: Confirm login success
    page.wait_for_selector("text=Welcome")
    print("Login successful!")

    browser.close()
