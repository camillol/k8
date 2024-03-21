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
from .v1_pod_failure_policy_on_exit_codes_requirement import V1PodFailurePolicyOnExitCodesRequirement
from .v1_pod_failure_policy_on_pod_conditions_pattern import V1PodFailurePolicyOnPodConditionsPattern

class V1PodFailurePolicyRule(BaseModel):
    """
    PodFailurePolicyRule describes how a pod failure is handled when the requirements are met. One of onExitCodes and onPodConditions, but not both, can be used in each rule.  # noqa: E501
    """
    action: StrictStr = Field(..., description="Specifies the action taken on a pod failure when the requirements are satisfied. Possible values are:  - FailJob: indicates that the pod's job is marked as Failed and all   running pods are terminated. - FailIndex: indicates that the pod's index is marked as Failed and will   not be restarted.   This value is beta-level. It can be used when the   `JobBackoffLimitPerIndex` feature gate is enabled (enabled by default). - Ignore: indicates that the counter towards the .backoffLimit is not   incremented and a replacement pod is created. - Count: indicates that the pod is handled in the default way - the   counter towards the .backoffLimit is incremented. Additional values are considered to be added in the future. Clients should react to an unknown action by skipping the rule.")
    on_exit_codes: Optional[V1PodFailurePolicyOnExitCodesRequirement] = Field(default=None, alias="onExitCodes")
    on_pod_conditions: Optional[conlist(V1PodFailurePolicyOnPodConditionsPattern)] = Field(default=None, alias="onPodConditions", description="Represents the requirement on the pod conditions. The requirement is represented as a list of pod condition patterns. The requirement is satisfied if at least one pattern matches an actual pod condition. At most 20 elements are allowed.")
    __properties = ["action", "onExitCodes", "onPodConditions"]

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
    def from_json(cls, json_str: str) -> V1PodFailurePolicyRule:
        """Create an instance of V1PodFailurePolicyRule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of on_exit_codes
        if self.on_exit_codes:
            _dict['onExitCodes'] = self.on_exit_codes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in on_pod_conditions (list)
        _items = []
        if self.on_pod_conditions:
            for _item in self.on_pod_conditions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['onPodConditions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1PodFailurePolicyRule:
        """Create an instance of V1PodFailurePolicyRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1PodFailurePolicyRule.parse_obj(obj)

        _obj = V1PodFailurePolicyRule.parse_obj({
            "action": obj.get("action"),
            "on_exit_codes": V1PodFailurePolicyOnExitCodesRequirement.from_dict(obj.get("onExitCodes")) if obj.get("onExitCodes") is not None else None,
            "on_pod_conditions": [V1PodFailurePolicyOnPodConditionsPattern.from_dict(_item) for _item in obj.get("onPodConditions")] if obj.get("onPodConditions") is not None else None
        })
        return _obj


