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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist

class V1NonResourceRule(BaseModel):
    """
    NonResourceRule holds information that describes a rule for the non-resource  # noqa: E501
    """
    non_resource_urls: Optional[conlist(StrictStr)] = Field(default=None, alias="nonResourceURLs", description="NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path.  \"*\" means all.")
    verbs: conlist(StrictStr) = Field(..., description="Verb is a list of kubernetes non-resource API verbs, like: get, post, put, delete, patch, head, options.  \"*\" means all.")
    __properties = ["nonResourceURLs", "verbs"]

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
    def from_json(cls, json_str: str) -> V1NonResourceRule:
        """Create an instance of V1NonResourceRule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1NonResourceRule:
        """Create an instance of V1NonResourceRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1NonResourceRule.parse_obj(obj)

        _obj = V1NonResourceRule.parse_obj({
            "non_resource_urls": obj.get("nonResourceURLs"),
            "verbs": obj.get("verbs")
        })
        return _obj


