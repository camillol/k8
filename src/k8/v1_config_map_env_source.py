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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class V1ConfigMapEnvSource(BaseModel):
    """
    ConfigMapEnvSource selects a ConfigMap to populate the environment variables with.  The contents of the target ConfigMap's Data field will represent the key-value pairs as environment variables.  # noqa: E501
    """
    name: Optional[StrictStr] = Field(default=None, description="Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names")
    optional: Optional[StrictBool] = Field(default=None, description="Specify whether the ConfigMap must be defined")
    __properties = ["name", "optional"]

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
    def from_json(cls, json_str: str) -> V1ConfigMapEnvSource:
        """Create an instance of V1ConfigMapEnvSource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ConfigMapEnvSource:
        """Create an instance of V1ConfigMapEnvSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ConfigMapEnvSource.parse_obj(obj)

        _obj = V1ConfigMapEnvSource.parse_obj({
            "name": obj.get("name"),
            "optional": obj.get("optional")
        })
        return _obj


