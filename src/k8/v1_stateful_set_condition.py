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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class V1StatefulSetCondition(BaseModel):
    """
    StatefulSetCondition describes the state of a statefulset at a certain point.  # noqa: E501
    """
    last_transition_time: Optional[datetime] = Field(default=None, alias="lastTransitionTime", description="Last time the condition transitioned from one status to another.")
    message: Optional[StrictStr] = Field(default=None, description="A human readable message indicating details about the transition.")
    reason: Optional[StrictStr] = Field(default=None, description="The reason for the condition's last transition.")
    status: StrictStr = Field(..., description="Status of the condition, one of True, False, Unknown.")
    type: StrictStr = Field(..., description="Type of statefulset condition.")
    __properties = ["lastTransitionTime", "message", "reason", "status", "type"]

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
    def from_json(cls, json_str: str) -> V1StatefulSetCondition:
        """Create an instance of V1StatefulSetCondition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1StatefulSetCondition:
        """Create an instance of V1StatefulSetCondition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1StatefulSetCondition.parse_obj(obj)

        _obj = V1StatefulSetCondition.parse_obj({
            "last_transition_time": obj.get("lastTransitionTime"),
            "message": obj.get("message"),
            "reason": obj.get("reason"),
            "status": obj.get("status"),
            "type": obj.get("type")
        })
        return _obj


