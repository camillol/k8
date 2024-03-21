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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class V1BoundObjectReference(BaseModel):
    """
    BoundObjectReference is a reference to an object that a token is bound to.  # noqa: E501
    """
    api_version: Optional[StrictStr] = Field(default=None, alias="apiVersion", description="API version of the referent.")
    kind: Optional[StrictStr] = Field(default=None, description="Kind of the referent. Valid kinds are 'Pod' and 'Secret'.")
    name: Optional[StrictStr] = Field(default=None, description="Name of the referent.")
    uid: Optional[StrictStr] = Field(default=None, description="UID of the referent.")
    __properties = ["apiVersion", "kind", "name", "uid"]

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
    def from_json(cls, json_str: str) -> V1BoundObjectReference:
        """Create an instance of V1BoundObjectReference from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1BoundObjectReference:
        """Create an instance of V1BoundObjectReference from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1BoundObjectReference.parse_obj(obj)

        _obj = V1BoundObjectReference.parse_obj({
            "api_version": obj.get("apiVersion"),
            "kind": obj.get("kind"),
            "name": obj.get("name"),
            "uid": obj.get("uid")
        })
        return _obj

