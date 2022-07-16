from typing import List

from bson import ObjectId
from pydantic import Field
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


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class FeatureTypeDefinition(BaseModel):
    feature: str
    feature_data_type: str


class ExpectedInputStructure(BaseModel):
    name: str
    type: str
    encoder: str


class ExpectedOutputStructure(BaseModel):
    name: str
    type: str


class Model(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    model_url: str = Field(...)
    name: str = Field(...)
    feature_type_definition: List[FeatureTypeDefinition]
    description: str = Field(...)
    version: str = Field(...)
    ludwig_version: str = Field(...)
    author: str = Field(...)
    namespace: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Bertv3",
                "feature_type_definition": [
                    {"feature": "name", "feature_data_type": "text"}
                ],
                "model_url": "/model/path/is/here",
                "description": "great nlp model",
                "version": "1.0",
                "ludwig_version": "1.0",
                "author": "ludwig_author",
                "namespace": "model_namespace",
            }
        }
