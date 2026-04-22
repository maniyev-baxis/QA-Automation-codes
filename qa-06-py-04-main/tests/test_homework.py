import pytest

from playwright.sync_api import expect


# py -m pytest -v --browser chromium --headed -q --tracing=on --video=on --html=reports/report.html --tags homework --slowmo 800
@pytest.mark.tags("homework")
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
def test_users_should_be_able_to_checkout(page, username, password):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill(username)
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill(password)
    page.locator("[data-test=\"login-button\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"checkout\"]").click()
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("bakhish")
    page.locator("[data-test=\"lastName\"]").click()
    page.locator("[data-test=\"lastName\"]").fill("maniyev")
    page.locator(".error-message-container").click()
    page.locator("[data-test=\"postalCode\"]").click()
    page.locator("[data-test=\"postalCode\"]").fill("19283")
    page.locator("[data-test=\"continue\"]").click()
    page.locator("[data-test=\"finish\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")
