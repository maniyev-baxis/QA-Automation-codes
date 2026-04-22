import os
from playwright.sync_api import sync_playwright
import pytest

# os.environ["DEBUG"] = "pw:api"
# os.environ["PWDEBUG"] = "1"




@pytest.fixture(scope="session")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, channel="msedge")
        # browser = p.webkit.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()
       





































