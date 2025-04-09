import pytest
from core.driver import Driver


# todo check if implementation is correct
@pytest.fixture(scope="function", autouse=True)
def setup_teardown(request):
    Driver().driver.get(Driver().base_url)
    yield
    Driver().quit()
