
import pytest

from playwright.sync_api import expect


@pytest.mark.tags("login")
@pytest.mark.parametrize(
    "username, password",
    [
        ("standard_user", "secret_sauce"),
        # ("locked_out_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
        ("error_user", "secret_sauce"),
        ("visual_user", "secret_sauce"),
    ],
)
def test_standart_users_shoulf_be_able_to_login(page, username, password):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill(username)
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill(password)
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")


# import pytest

# from playwright.sync_api import expect


# # py -m pytest -v --browser chromium --headed -q --tracing=on --video=on --html=reports/report.html --tags homework --slowmo 800
# @pytest.mark.tags("homework")
# @pytest.mark.parametrize(
#     "username, password",
#     [
#         ("standard_user", "secret_sauce"),
#         ("locked_out_user", "secret_sauce"),
#         ("problem_user", "secret_sauce"),
#         ("performance_glitch_user", "secret_sauce"),
#         ("error_user", "secret_sauce"),
#         ("visual_user", "secret_sauce"),
#     ],
# )
# def test_users_should_be_able_to_checkout(page, username, password):
#     page.goto("https://www.saucedemo.com/")
#     page.locator("[data-test=\"username\"]").click()
#     page.locator("[data-test=\"username\"]").click()
#     page.locator("[data-test=\"username\"]").fill(username)
#     page.locator("[data-test=\"password\"]").click()
#     page.locator("[data-test=\"password\"]").fill(password)
#     page.locator("[data-test=\"login-button\"]").click()
#     expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")


import pytest
from playwright.sync_api import sync_playwright
import time


class TestSauceDemoTwoBrowsers:

    @pytest.fixture(scope="function")
    def two_logged_in_browsers(self):
        with sync_playwright() as p:
            browser1 = p.chromium.launch(headless=False)
            browser2 = p.chromium.launch(headless=False)

            context1 = browser1.new_context()
            context2 = browser2.new_context()

            page1 = context1.new_page()
            page2 = context2.new_page()

            login_url = "https://www.saucedemo.com/"

            for page in [page1, page2]:
                page.goto(login_url)
                page.locator("[data-test=\"username\"]").fill("standard_user")
                page.locator("[data-test=\"password\"]").fill("secret_sauce")
                page.locator("[data-test=\"login-button\"]").click()
                page.wait_for_timeout(2000)

            yield page1, page2

            browser1.close()
            browser2.close()

    def test_cart_sync_within_one_second(self, two_logged_in_browsers):
        page1, page2 = two_logged_in_browsers

        page1.locator(
            "[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
        print("Məhsul 1-ci brauzerdə səbətə əlavə edildi")

        start = time.time()
        success = False

        while time.time() - start < 1.0:
            try:
                badge = page2.locator("[data-test=\"shopping-cart-badge\"]")
                if badge.is_visible() and badge.text_content() == "1":
                    success = True
                    elapsed = (time.time() - start) * 1000
                    print(f" Səbət {elapsed:.0f}ms-də sinxronlaşdı!")
                    break
            except:
                pass
            page2.wait_for_timeout(50)

        assert success, " Məhsul 1 saniyə ərzində 2-ci brauzerin səbətində görünmədi!"
        print(" TEST Passed")




