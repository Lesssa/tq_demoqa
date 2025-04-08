import json
import os

from models.conf import Config


class ConfigManager:
    _config: Config = None

    @staticmethod
    def __load_config():
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        config_path = os.path.join(project_root, 'config', 'config.json')
        with open(config_path, "r", encoding="utf-8") as f:
            ConfigManager._config = Config(**json.load(f))

    @staticmethod
    def get(key):
        if ConfigManager._config is None:
            ConfigManager.__load_config()
        config_dict = ConfigManager._config.__dict__
        keys = key.split(".")
        value = config_dict

        for key in keys:
            if isinstance(value, dict):
                value = value.get(key)
            else:
                value = getattr(value, key, None)

            if value is None:
                raise KeyError(f"Key path '{key}' not found in config")

        return value
