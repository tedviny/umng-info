from pydantic import BaseModel


class Info(BaseModel):
    info: str
    last_update: str
    author: str