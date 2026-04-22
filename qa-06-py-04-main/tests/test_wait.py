import pytest

#
# Waits (https://playwright.dev/python/docs/actionability)
#
# Explicit wait - wait for a specific condition to occur before proceeding further in the code. 
# Implicit wait - set a default waiting time for the entire test script, which will be applied
#                 to all elements when trying to find them.
#
# No implicit waits in Playwright (different approach) => --slowmo 800 (800ms delay between each action)
# Explicit waits in Playwright =>  https://playwright.dev/python/docs/api/class-locator#locator-wait-for
#
# page.locator("selector").wait_for(state="(visible|hidden|attached|detached)", timeout=30000) 
# page.locator("selector").wait_for(state="visible") - Waits for the element to be visible on the page.
# page.locator("selector").wait_for(state="hidden") - Waits for the element to be hidden on the page.
# page.locator("selector").wait_for(state="attached") - Waits for the element to be present in the DOM.
# page.locator("selector").wait_for(state="detached") - Waits for the element to be removed from the DOM.
# page.wait_for_timeout(5000) - Waits for 5 seconds (https://playwright.dev/python/docs/api/class-page#page-wait-for-timeout)
# https://playwright.dev/python/docs/api/class-page#page-wait-for-event-2
#

# py -m pytest -v --browser chromium --headed -q --tracing=on --video=on --html=reports/report.html --tags homework --slowmo 800
@pytest.mark.tags("homework")
def test_users_should_be_able_to_checkout(page):
    page.wait_for_timeout(5000)
