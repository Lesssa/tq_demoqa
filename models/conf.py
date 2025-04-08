from pydantic import BaseModel


class Config(BaseModel):
    base_url: str
    browser: str
    browser_options: dict
    waiting_time: int
