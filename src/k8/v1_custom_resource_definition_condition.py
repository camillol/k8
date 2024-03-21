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

class V1CustomResourceDefinitionCondition(BaseModel):
    """
    CustomResourceDefinitionCondition contains details for the current condition of this pod.  # noqa: E501
    """
    last_transition_time: Optional[datetime] = Field(default=None, alias="lastTransitionTime", description="lastTransitionTime last time the condition transitioned from one status to another.")
    message: Optional[StrictStr] = Field(default=None, description="message is a human-readable message indicating details about last transition.")
    reason: Optional[StrictStr] = Field(default=None, description="reason is a unique, one-word, CamelCase reason for the condition's last transition.")
    status: StrictStr = Field(..., description="status is the status of the condition. Can be True, False, Unknown.")
    type: StrictStr = Field(..., description="type is the type of the condition. Types include Established, NamesAccepted and Terminating.")
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
    def from_json(cls, json_str: str) -> V1CustomResourceDefinitionCondition:
        """Create an instance of V1CustomResourceDefinitionCondition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1CustomResourceDefinitionCondition:
        """Create an instance of V1CustomResourceDefinitionCondition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1CustomResourceDefinitionCondition.parse_obj(obj)

        _obj = V1CustomResourceDefinitionCondition.parse_obj({
            "last_transition_time": obj.get("lastTransitionTime"),
            "message": obj.get("message"),
            "reason": obj.get("reason"),
            "status": obj.get("status"),
            "type": obj.get("type")
        })
        return _obj


