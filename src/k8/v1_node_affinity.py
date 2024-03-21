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
from .v1_node_selector import V1NodeSelector
from .v1_preferred_scheduling_term import V1PreferredSchedulingTerm

class V1NodeAffinity(BaseModel):
    """
    Node affinity is a group of node affinity scheduling rules.  # noqa: E501
    """
    preferred_during_scheduling_ignored_during_execution: Optional[conlist(V1PreferredSchedulingTerm)] = Field(default=None, alias="preferredDuringSchedulingIgnoredDuringExecution", description="The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding \"weight\" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.")
    required_during_scheduling_ignored_during_execution: Optional[V1NodeSelector] = Field(default=None, alias="requiredDuringSchedulingIgnoredDuringExecution")
    __properties = ["preferredDuringSchedulingIgnoredDuringExecution", "requiredDuringSchedulingIgnoredDuringExecution"]

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
    def from_json(cls, json_str: str) -> V1NodeAffinity:
        """Create an instance of V1NodeAffinity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in preferred_during_scheduling_ignored_during_execution (list)
        _items = []
        if self.preferred_during_scheduling_ignored_during_execution:
            for _item in self.preferred_during_scheduling_ignored_during_execution:
                if _item:
                    _items.append(_item.to_dict())
            _dict['preferredDuringSchedulingIgnoredDuringExecution'] = _items
        # override the default output from pydantic by calling `to_dict()` of required_during_scheduling_ignored_during_execution
        if self.required_during_scheduling_ignored_during_execution:
            _dict['requiredDuringSchedulingIgnoredDuringExecution'] = self.required_during_scheduling_ignored_during_execution.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1NodeAffinity:
        """Create an instance of V1NodeAffinity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1NodeAffinity.parse_obj(obj)

        _obj = V1NodeAffinity.parse_obj({
            "preferred_during_scheduling_ignored_during_execution": [V1PreferredSchedulingTerm.from_dict(_item) for _item in obj.get("preferredDuringSchedulingIgnoredDuringExecution")] if obj.get("preferredDuringSchedulingIgnoredDuringExecution") is not None else None,
            "required_during_scheduling_ignored_during_execution": V1NodeSelector.from_dict(obj.get("requiredDuringSchedulingIgnoredDuringExecution")) if obj.get("requiredDuringSchedulingIgnoredDuringExecution") is not None else None
        })
        return _obj

