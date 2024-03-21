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
from .v1_env_var_source import V1EnvVarSource

class V1EnvVar(BaseModel):
    """
    EnvVar represents an environment variable present in a Container.  # noqa: E501
    """
    name: StrictStr = Field(..., description="Name of the environment variable. Must be a C_IDENTIFIER.")
    value: Optional[StrictStr] = Field(default=None, description="Variable references $(VAR_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \"$$(VAR_NAME)\" will produce the string literal \"$(VAR_NAME)\". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to \"\".")
    value_from: Optional[V1EnvVarSource] = Field(default=None, alias="valueFrom")
    __properties = ["name", "value", "valueFrom"]

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
    def from_json(cls, json_str: str) -> V1EnvVar:
        """Create an instance of V1EnvVar from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of value_from
        if self.value_from:
            _dict['valueFrom'] = self.value_from.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1EnvVar:
        """Create an instance of V1EnvVar from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1EnvVar.parse_obj(obj)

        _obj = V1EnvVar.parse_obj({
            "name": obj.get("name"),
            "value": obj.get("value"),
            "value_from": V1EnvVarSource.from_dict(obj.get("valueFrom")) if obj.get("valueFrom") is not None else None
        })
        return _obj


