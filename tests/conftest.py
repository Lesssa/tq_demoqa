import pytest
from config.config_manager import ConfigManager
from core.driver import Driver


@pytest.fixture(scope="session", autouse=True)
def setup_environment(request):
    ConfigManager.load_config()

    def cleanup():
        driver = Driver()
        driver.quit()

    request.addfinalizer(cleanup)
    yield


