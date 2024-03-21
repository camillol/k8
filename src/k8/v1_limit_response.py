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
from .v1_queuing_configuration import V1QueuingConfiguration

class V1LimitResponse(BaseModel):
    """
    LimitResponse defines how to handle requests that can not be executed right now.  # noqa: E501
    """
    queuing: Optional[V1QueuingConfiguration] = None
    type: StrictStr = Field(..., description="`type` is \"Queue\" or \"Reject\". \"Queue\" means that requests that can not be executed upon arrival are held in a queue until they can be executed or a queuing limit is reached. \"Reject\" means that requests that can not be executed upon arrival are rejected. Required.")
    __properties = ["queuing", "type"]

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
    def from_json(cls, json_str: str) -> V1LimitResponse:
        """Create an instance of V1LimitResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of queuing
        if self.queuing:
            _dict['queuing'] = self.queuing.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1LimitResponse:
        """Create an instance of V1LimitResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1LimitResponse.parse_obj(obj)

        _obj = V1LimitResponse.parse_obj({
            "queuing": V1QueuingConfiguration.from_dict(obj.get("queuing")) if obj.get("queuing") is not None else None,
            "type": obj.get("type")
        })
        return _obj


