import json
import os
from typing import List

from pydantic import BaseModel, Field, ConfigDict, TypeAdapter


class User(BaseModel):
    first_name: str = Field(alias="firstName", title="First Name")
    last_name: str = Field(alias="lastName", title="Last Name")
    user_email: str = Field(alias="userEmail", title="Email")
    age: int = Field(alias="age", title="Age")
    salary: int = Field(alias="salary", title="Salary")
    department: str = Field(alias="department", title="Department")

    @classmethod
    def load_all(cls) -> List["User"]:
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        file_path = os.path.join(project_root, "tests", "users.json")
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        return [cls(**user) for user in data]
