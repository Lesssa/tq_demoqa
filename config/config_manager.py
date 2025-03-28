import json


class ConfigManager:
    _config = None

    @staticmethod
    def load_config():
        with open("../config/config.json", "r", encoding="utf-8") as f:
            ConfigManager._config = json.load(f)

    @staticmethod
    def get(key):
        if ConfigManager._config is None:
            ConfigManager.load_config()
        return ConfigManager._config.get(key)
