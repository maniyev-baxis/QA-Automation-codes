import time
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

# Enable codegen for debugging
# import os
# os.environ["PWDEBUG"] = "1"


# Har viewers - https://toolbox.googleapps.com/apps/har_analyzer/
# Trace viewers - https://trace.playwright.dev/
# py -m pytest -v --browser chromium --headed -q --tracing=on --video=on --html=reports/report.html --tags login_pom --slowmo 800
# py -m pytest -v --browser firefox --headed -q --tracing=on --video=on --html=reports/report.html
# py -m pytest -v --browser webkit --headed -q --tracing=on --video=on --html=reports/report.html
# Docs: https://playwright.dev/python/docs/test-runners
@pytest.fixture(scope="function")
def context(browser):
    TIMESTAMP = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())

    context = browser.new_context(
        viewport={"width": 1280, "height": 720},
        is_mobile=False,
        locale="en-US",
        java_script_enabled=True,
        record_video_dir=f"reports/artifact_{TIMESTAMP}",
        record_har_path=f"reports/artifact_{TIMESTAMP}/network.har",
        record_har_mode="full"
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context
    context.tracing.stop(path=f"reports/artifact_{TIMESTAMP}/trace.zip")
    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="function")
def login_page(page):
    login_page = LoginPage(page)
    yield login_page

@pytest.fixture(scope="function")
def products_page(page):
    products_page = ProductsPage(page)
    yield products_page
       





































