import os
from playwright.sync_api import sync_playwright
import pytest

os.environ["DEBUG"] = "pw:api"
os.environ["PWDEBUG"] = "1"


BASE_URL = "https://www.saucedemo.com"

@pytest.fixture(scope="session")
def saucedemo_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(BASE_URL)
        yield page
        browser.close()
       





































