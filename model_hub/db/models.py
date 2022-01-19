from typing import Optional

from bson import ObjectId
from pydantic.main import BaseModel


class OID(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if v == "":
            raise TypeError("ObjectId is empty")
        if ObjectId.is_valid(v) is False:
            raise TypeError("ObjectId invalid")
        return str(v)


class BaseDBModel(BaseModel):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True

        @classmethod
        def alias_generator(cls, string: str) -> str:
            """Camel case generator."""
            temp = string.split("_")
            return temp[0] + "".join(ele.title() for ele in temp[1:])


class Model(BaseDBModel):
    id: Optional[OID]
    model_url: str
    name: str
    description: str
    version: str
    ludwig_version: str
    author: str
    namespace: str
