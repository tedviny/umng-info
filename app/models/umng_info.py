from pydantic import BaseModel


class Info(BaseModel):
    info: str
    last_updated: str
    author: str