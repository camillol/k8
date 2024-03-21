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

class V1PodReadinessGate(BaseModel):
    """
    PodReadinessGate contains the reference to a pod condition  # noqa: E501
    """
    condition_type: StrictStr = Field(..., alias="conditionType", description="ConditionType refers to a condition in the pod's condition list with matching type.")
    __properties = ["conditionType"]

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
    def from_json(cls, json_str: str) -> V1PodReadinessGate:
        """Create an instance of V1PodReadinessGate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1PodReadinessGate:
        """Create an instance of V1PodReadinessGate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1PodReadinessGate.parse_obj(obj)

        _obj = V1PodReadinessGate.parse_obj({
            "condition_type": obj.get("conditionType")
        })
        return _obj


