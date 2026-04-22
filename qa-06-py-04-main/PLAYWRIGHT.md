# Playwright Python Cheat Sheet

This is a step-by-step guide with practical code snippets and quick references for Playwright in Python.

## 1) Install and setup

### Install packages

```bash
pip install playwright pytest pytest-playwright
```

### Install browsers

```bash
playwright install
```

### Minimal test layout

```
tests/
  conftest.py
  test_login.py
```

### Minimal test example

```python
def test_home(page):
	page.goto("https://example.com")
	assert page.title() == "Example Domain"
```

Run:

```bash
pytest -q
```

## 2) Core concepts (quick map)

- **Browser**: The installed engine (Chromium, Firefox, WebKit).
- **BrowserContext**: An isolated session (cookies, storage). Use one per test for isolation.
- **Page**: A single tab in a context.
- **Locator**: A smart handle for finding elements; auto-waits and retries.
- **Assertions**: Use `expect()` for auto-waiting checks.

## 3) Browsers and contexts

### Run on a specific browser

```bash
pytest -q --browser chromium
pytest -q --browser firefox
pytest -q --browser webkit
```

### Headed vs headless

```bash
pytest -q --headed
```

### Multiple browsers in one run

```bash
pytest -q --browser chromium --browser firefox
```

### Custom context options (conftest.py)

```python
import pytest

@pytest.fixture(scope="function")
def context(browser):
	context = browser.new_context(
		viewport={"width": 1280, "height": 720},
		locale="en-US",
		timezone_id="UTC",
	)
	yield context
	context.close()

@pytest.fixture(scope="function")
def page(context):
	page = context.new_page()
	yield page
	page.close()
```

## 4) Locators: what and why

### What is a locator

`locator` is Playwright's main element-finding API. It is **lazy**, **retryable**, and **auto-waiting**.
Instead of finding elements once, it re-finds them when you use it, which avoids flakiness.

### Recommended order of preference

1. **Role-based** (`get_by_role`) - closest to user behavior
2. **Label-based** (`get_by_label`) - for inputs tied to labels
3. **Placeholder** (`get_by_placeholder`)
4. **Text** (`get_by_text`)
5. **Alt/Title** (`get_by_alt_text`, `get_by_title`)
6. **Test ID** (`get_by_test_id`) - stable automation IDs
7. **CSS/XPath** - last resort

## 5) Selector types (with examples)

### HTML sample

```html
<button class="btn primary" data-test="save" aria-label="Save changes">
  Save
</button>

<label for="email">Email</label>
<input id="email" name="email" placeholder="you@example.com" />

<img src="logo.png" alt="Company Logo" />

<div role="alert">Error: invalid password</div>
```

### Role selector

```python
page.get_by_role("button", name="Save").click()
page.get_by_role("alert").to_contain_text("invalid password")
```

### Label selector

```python
page.get_by_label("Email").fill("user@example.com")
```

### Placeholder selector

```python
page.get_by_placeholder("you@example.com").fill("user@example.com")
```

### Text selector

```python
page.get_by_text("Save").click()
```

### Alt text selector

```python
page.get_by_alt_text("Company Logo").is_visible()
```

### Title selector

```python
page.get_by_title("Help").click()
```

### Test id selector

```python
page.get_by_test_id("save").click()
```

### CSS selector (last resort)

```python
page.locator("button.btn.primary").click()
page.locator("input#email").fill("user@example.com")
```

### XPath selector (avoid unless needed)

```python
page.locator("//button[contains(., 'Save')]").click()
```

## 6) Locator patterns (advanced)

```python
row = page.get_by_role("row", name="Alice")
row.get_by_role("button", name="Edit").click()

page.locator(".card").filter(has_text="Pro").click()
page.locator(".card").filter(has=page.get_by_role("button", name="Buy")).click()

page.get_by_role("listitem").nth(2).click()
```

## 7) Actions (click, type, select)

```python
page.click("text=Sign in")
page.fill("input[name='email']", "user@example.com")
page.type("input[name='password']", "secret")
page.check("input[type='checkbox']")
page.uncheck("input[type='checkbox']")
page.select_option("select#country", "US")
page.hover(".menu")
page.focus("input#search")
page.press("input#search", "Enter")
```

## 8) Assertions (auto-waiting)

```python
from playwright.sync_api import expect

expect(page).to_have_url("https://example.com/dashboard")
expect(page).to_have_title("Dashboard")
expect(page.get_by_role("heading", name="Welcome")).to_be_visible()
expect(page.locator(".toast")).to_contain_text("Saved")
```

## 9) Waiting rules (avoid explicit sleeps)

- Playwright auto-waits for elements to be ready.
- Use `expect()` for UI to settle.
- Only use `wait_for_timeout()` for debugging.

```python
page.get_by_role("button", name="Save").click()
expect(page.locator(".toast")).to_be_visible()

page.wait_for_load_state("networkidle")
```

## 10) Navigation and URL control

```python
page.goto("https://example.com")
page.go_back()
page.go_forward()
page.reload()
expect(page).to_have_url(r".*/dashboard")
```

## 11) Forms and inputs

```python
page.get_by_label("Email").fill("user@example.com")
page.get_by_label("Password").fill("secret")
page.get_by_role("button", name="Sign in").click()
```

## 12) Dialogs, alerts, confirms

```python
page.once("dialog", lambda dialog: dialog.accept())
page.get_by_role("button", name="Delete").click()
```

## 13) Frames and iframes

```python
frame = page.frame(name="payment")
frame.get_by_label("Card number").fill("4242 4242 4242 4242")
```

## 14) File upload and download

```python
page.set_input_files("input[type='file']", "tests/data/avatar.png")

with page.expect_download() as download_info:
	page.get_by_role("button", name="Download").click()

download = download_info.value
download.save_as("reports/download.pdf")
```

## 15) Multiple pages / tabs

```python
with context.expect_page() as new_page_info:
	page.get_by_role("link", name="Open in new tab").click()

new_page = new_page_info.value
expect(new_page).to_have_title("Details")
```

## 16) Authentication and storage state

### Save authenticated state

```python
page.goto("https://example.com/login")
page.get_by_label("Email").fill("user@example.com")
page.get_by_label("Password").fill("secret")
page.get_by_role("button", name="Sign in").click()
expect(page).to_have_url("https://example.com/app")
page.context.storage_state(path="reports/auth.json")
```

### Reuse authenticated state

```python
context = browser.new_context(storage_state="reports/auth.json")
page = context.new_page()
page.goto("https://example.com/app")
```

## 17) Network control and API mocking

```python
page.route("**/api/users", lambda route: route.fulfill(
	status=200,
	content_type="application/json",
	body='{"items": []}'
))

page.route("**/*.{png,jpg}", lambda route: route.abort())
```

## 18) API testing (no browser)

```python
from playwright.sync_api import sync_playwright

def test_api():
	with sync_playwright() as p:
		request = p.request.new_context(base_url="https://api.example.com")
		response = request.get("/health")
		assert response.status == 200
		request.dispose()
```

## 19) Screenshots, video, tracing

### Screenshot

```python
page.screenshot(path="reports/screenshot.png", full_page=True)
```

### Video (context option)

```python
context = browser.new_context(
	record_video_dir="reports/videos",
	record_video_size={"width": 1280, "height": 720},
)
```

### Video with pytest-playwright (CLI)

```bash
pytest -q --video=on
pytest -q --video=retain-on-failure
```

### Custom video per test (fixture)

```python
import pytest

@pytest.fixture(scope="function")
def context(browser):
	context = browser.new_context(record_video_dir="reports/videos")
	yield context
	context.close()
```

### Tracing

```python
context.tracing.start(screenshots=True, snapshots=True, sources=True)
page.goto("https://example.com")
context.tracing.stop(path="reports/trace.zip")
```

### Tracing with pytest-playwright (CLI)

```bash
pytest -q --tracing=on
pytest -q --tracing=retain-on-failure
```

### View a trace

```bash
playwright show-trace reports/trace.zip
```

### Keep artifacts only on failure

```bash
pytest -q --video=retain-on-failure --tracing=retain-on-failure --screenshot=only-on-failure
```

## 20) Mobile emulation

```python
iphone = browser.new_context(
	viewport={"width": 390, "height": 844},
	user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)",
	is_mobile=True,
	has_touch=True,
)
page = iphone.new_page()
page.goto("https://example.com")
```

## 21) Page Object Model (lightweight)

```python
class LoginPage:
	def __init__(self, page):
		self.page = page
		self.username = page.get_by_label("Username")
		self.password = page.get_by_label("Password")
		self.login_button = page.get_by_role("button", name="Login")

	def login(self, username, password):
		self.username.fill(username)
		self.password.fill(password)
		self.login_button.click()
```

## 22) Common pitfalls and fixes

- Use `expect()` instead of manual sleeps.
- Prefer `get_by_role` and `get_by_label` over CSS.
- Avoid `page.wait_for_timeout()` in real tests.
- Use `storage_state` for fast authenticated tests.
- Use `page.route()` to control unstable endpoints.

## 23) Full login example (similar to your test)

```python
import pytest
from playwright.sync_api import expect

@pytest.mark.parametrize(
	"username, password",
	[
		("standard_user", "secret_sauce"),
		("problem_user", "secret_sauce"),
	],
)
def test_users_can_login(page, username, password):
	page.goto("https://www.saucedemo.com/")
	page.get_by_test_id("username").fill(username)
	page.get_by_test_id("password").fill(password)
	page.get_by_test_id("login-button").click()
	expect(page.get_by_test_id("title")).to_contain_text("Products")
```