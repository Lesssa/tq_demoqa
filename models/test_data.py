import json
import os

from pydantic import BaseModel


class TestData(BaseModel):
    alert_text: str
    confirm_alert_text: str
    after_confirm_text: str
    prompt_alert_text: str
    name_to_prompt: str
    after_prompt_text: str

    @classmethod
    def load_from_json(cls) -> 'TestData':
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        file_path = os.path.join(project_root, "tests", "test_data.json")
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls(**data)
