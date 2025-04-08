import pytest
from config.config_manager import ConfigManager
from core.driver import Driver


# todo check if implementation is correct
@pytest.fixture(scope="function", autouse=True)
def setup_environment(request):
    Driver().driver.get(Driver().base_url)
    yield
    Driver().quit()
