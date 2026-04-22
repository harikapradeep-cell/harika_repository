import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.fixture(scope="session")
def browser():
    """Fixture to create a browser instance for the session"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


def test_signup_button_exists(page):
    """Test that validates a signup button is available on the website"""
    # Navigate to the website
    page.goto("https://rahulshettyacademy.com/")


    # Wait for page to load
page.wait_for_load_state("networkidle")

 # Try to find signup button by multiple selectors
 # Looking for common signup button patterns
 signup_selectors = [
      "button:has-text('Sign Up')",
      "button:has-text('SIGN UP')",
        "a:has-text('Sign Up')",
        "a:has-text('SIGN UP')",
        "//button[contains(text(), 'Sign')]",
        "//a[contains(text(), 'Sign')]",
        "[aria-label*='sign up' i]",
        "[class*='signup' i]",
      ]

  # Check if signup button exists
  signup_button = None
   for selector in signup_selectors:
        try:
            element = page.locator(selector).first
            if element.is_visible():
                signup_button = element
                print(f"Found signup button with selector: {selector}")
                break
        except Exception:
            pass

    # Assert that signup button is found
    assert signup_button is not None, "Signup button not found on the page"

    # Additional validation - verify the button is visible and enabled
    expect(signup_button).to_be_visible()
    print("Signup button is visible and available on the page")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
