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
from pydantic import BaseModel, Field, StrictInt
from .v1_label_selector import V1LabelSelector
from .v1_pod_template_spec import V1PodTemplateSpec

class V1ReplicaSetSpec(BaseModel):
    """
    ReplicaSetSpec is the specification of a ReplicaSet.  # noqa: E501
    """
    min_ready_seconds: Optional[StrictInt] = Field(default=None, alias="minReadySeconds", description="Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)")
    replicas: Optional[StrictInt] = Field(default=None, description="Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller")
    selector: V1LabelSelector = Field(...)
    template: Optional[V1PodTemplateSpec] = None
    __properties = ["minReadySeconds", "replicas", "selector", "template"]

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
    def from_json(cls, json_str: str) -> V1ReplicaSetSpec:
        """Create an instance of V1ReplicaSetSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of selector
        if self.selector:
            _dict['selector'] = self.selector.to_dict()
        # override the default output from pydantic by calling `to_dict()` of template
        if self.template:
            _dict['template'] = self.template.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ReplicaSetSpec:
        """Create an instance of V1ReplicaSetSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ReplicaSetSpec.parse_obj(obj)

        _obj = V1ReplicaSetSpec.parse_obj({
            "min_ready_seconds": obj.get("minReadySeconds"),
            "replicas": obj.get("replicas"),
            "selector": V1LabelSelector.from_dict(obj.get("selector")) if obj.get("selector") is not None else None,
            "template": V1PodTemplateSpec.from_dict(obj.get("template")) if obj.get("template") is not None else None
        })
        return _obj


