import json
import os

from pydantic import BaseModel


class FrameTestData(BaseModel):
    parent_text: str
    child_text: str
    sample_text: str

    @classmethod
    def load_from_json(cls) -> 'FrameTestData':
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        file_path = os.path.join(project_root, "tests", "frame_test_data.json")
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls(**data)
