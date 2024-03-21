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
from .v1_pod_affinity_term import V1PodAffinityTerm
from .v1_weighted_pod_affinity_term import V1WeightedPodAffinityTerm

class V1PodAffinity(BaseModel):
    """
    Pod affinity is a group of inter pod affinity scheduling rules.  # noqa: E501
    """
    preferred_during_scheduling_ignored_during_execution: Optional[conlist(V1WeightedPodAffinityTerm)] = Field(default=None, alias="preferredDuringSchedulingIgnoredDuringExecution", description="The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding \"weight\" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.")
    required_during_scheduling_ignored_during_execution: Optional[conlist(V1PodAffinityTerm)] = Field(default=None, alias="requiredDuringSchedulingIgnoredDuringExecution", description="If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.")
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
    def from_json(cls, json_str: str) -> V1PodAffinity:
        """Create an instance of V1PodAffinity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in required_during_scheduling_ignored_during_execution (list)
        _items = []
        if self.required_during_scheduling_ignored_during_execution:
            for _item in self.required_during_scheduling_ignored_during_execution:
                if _item:
                    _items.append(_item.to_dict())
            _dict['requiredDuringSchedulingIgnoredDuringExecution'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1PodAffinity:
        """Create an instance of V1PodAffinity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1PodAffinity.parse_obj(obj)

        _obj = V1PodAffinity.parse_obj({
            "preferred_during_scheduling_ignored_during_execution": [V1WeightedPodAffinityTerm.from_dict(_item) for _item in obj.get("preferredDuringSchedulingIgnoredDuringExecution")] if obj.get("preferredDuringSchedulingIgnoredDuringExecution") is not None else None,
            "required_during_scheduling_ignored_during_execution": [V1PodAffinityTerm.from_dict(_item) for _item in obj.get("requiredDuringSchedulingIgnoredDuringExecution")] if obj.get("requiredDuringSchedulingIgnoredDuringExecution") is not None else None
        })
        return _obj


