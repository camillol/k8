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
from .v1_daemon_set_update_strategy import V1DaemonSetUpdateStrategy
from .v1_label_selector import V1LabelSelector
from .v1_pod_template_spec import V1PodTemplateSpec

class V1DaemonSetSpec(BaseModel):
    """
    DaemonSetSpec is the specification of a daemon set.  # noqa: E501
    """
    min_ready_seconds: Optional[StrictInt] = Field(default=None, alias="minReadySeconds", description="The minimum number of seconds for which a newly created DaemonSet pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready).")
    revision_history_limit: Optional[StrictInt] = Field(default=None, alias="revisionHistoryLimit", description="The number of old history to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.")
    selector: V1LabelSelector = Field(...)
    template: V1PodTemplateSpec = Field(...)
    update_strategy: Optional[V1DaemonSetUpdateStrategy] = Field(default=None, alias="updateStrategy")
    __properties = ["minReadySeconds", "revisionHistoryLimit", "selector", "template", "updateStrategy"]

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
    def from_json(cls, json_str: str) -> V1DaemonSetSpec:
        """Create an instance of V1DaemonSetSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of update_strategy
        if self.update_strategy:
            _dict['updateStrategy'] = self.update_strategy.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1DaemonSetSpec:
        """Create an instance of V1DaemonSetSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1DaemonSetSpec.parse_obj(obj)

        _obj = V1DaemonSetSpec.parse_obj({
            "min_ready_seconds": obj.get("minReadySeconds"),
            "revision_history_limit": obj.get("revisionHistoryLimit"),
            "selector": V1LabelSelector.from_dict(obj.get("selector")) if obj.get("selector") is not None else None,
            "template": V1PodTemplateSpec.from_dict(obj.get("template")) if obj.get("template") is not None else None,
            "update_strategy": V1DaemonSetUpdateStrategy.from_dict(obj.get("updateStrategy")) if obj.get("updateStrategy") is not None else None
        })
        return _obj


