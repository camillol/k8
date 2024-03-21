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
from pydantic import BaseModel, Field, conlist
from .v1beta3_flow_schema_condition import V1beta3FlowSchemaCondition

class V1beta3FlowSchemaStatus(BaseModel):
    """
    FlowSchemaStatus represents the current state of a FlowSchema.  # noqa: E501
    """
    conditions: Optional[conlist(V1beta3FlowSchemaCondition)] = Field(default=None, description="`conditions` is a list of the current states of FlowSchema.")
    __properties = ["conditions"]

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
    def from_json(cls, json_str: str) -> V1beta3FlowSchemaStatus:
        """Create an instance of V1beta3FlowSchemaStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in conditions (list)
        _items = []
        if self.conditions:
            for _item in self.conditions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['conditions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1beta3FlowSchemaStatus:
        """Create an instance of V1beta3FlowSchemaStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1beta3FlowSchemaStatus.parse_obj(obj)

        _obj = V1beta3FlowSchemaStatus.parse_obj({
            "conditions": [V1beta3FlowSchemaCondition.from_dict(_item) for _item in obj.get("conditions")] if obj.get("conditions") is not None else None
        })
        return _obj


