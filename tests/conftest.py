import pytest
from playwright.sync_api import Page, Playwright


@pytest.fixture  # дефолтный scope='function'
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()
