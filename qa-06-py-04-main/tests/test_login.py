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
def test_users_should_be_able_to_login(page, username, password):
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').click()
    page.locator('[data-test="username"]').fill(username)
    page.locator('[data-test="password"]').click()
    page.locator('[data-test="password"]').fill(password)
    page.locator('[data-test="login-button"]').click()
    expect(page.locator('[data-test="title"]')).to_contain_text("Products")


@pytest.mark.tags("login_pom")
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
def test_users_should_not_be_able_to_login_using_pom(
    login_page, products_page, username, password
):
    login_page.visit()
    login_page.login(username, password)
    expect(products_page.title_heading).to_contain_text("Products")
