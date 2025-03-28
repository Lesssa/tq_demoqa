import pytest
from config.config_manager import ConfigManager


@pytest.fixture(scope="session", autouse=True)
def setup_environment():
    """Настраивает окружение перед тестами"""
    ConfigManager.load_config()  # Загружаем конфиг перед тестами
    yield
    # Если нужны действия после всех тестов, их можно добавить здесь

