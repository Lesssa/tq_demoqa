import pytest
from core.browser import Browser


@pytest.fixture(scope="function", autouse=True)
def browser():
    driver = Browser().get_driver()
    yield driver
    Browser().quit()
