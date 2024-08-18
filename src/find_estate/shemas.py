from pydantic import BaseModel


class QueryModel(BaseModel):
    cadastral_num: str
    latitude: str | None = None
    longitude: str | None = None