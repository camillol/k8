# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.29
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr

class V1beta3UserSubject(BaseModel):
    """
    UserSubject holds detailed information for user-kind subject.  # noqa: E501
    """
    name: StrictStr = Field(..., description="`name` is the username that matches, or \"*\" to match all usernames. Required.")
    __properties = ["name"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> V1beta3UserSubject:
        """Create an instance of V1beta3UserSubject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1beta3UserSubject:
        """Create an instance of V1beta3UserSubject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1beta3UserSubject.parse_obj(obj)

        _obj = V1beta3UserSubject.parse_obj({
            "name": obj.get("name")
        })
        return _obj


