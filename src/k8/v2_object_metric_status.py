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



from pydantic import BaseModel, Field
from .v2_cross_version_object_reference import V2CrossVersionObjectReference
from .v2_metric_identifier import V2MetricIdentifier
from .v2_metric_value_status import V2MetricValueStatus

class V2ObjectMetricStatus(BaseModel):
    """
    ObjectMetricStatus indicates the current value of a metric describing a kubernetes object (for example, hits-per-second on an Ingress object).  # noqa: E501
    """
    current: V2MetricValueStatus = Field(...)
    described_object: V2CrossVersionObjectReference = Field(..., alias="describedObject")
    metric: V2MetricIdentifier = Field(...)
    __properties = ["current", "describedObject", "metric"]

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
    def from_json(cls, json_str: str) -> V2ObjectMetricStatus:
        """Create an instance of V2ObjectMetricStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of current
        if self.current:
            _dict['current'] = self.current.to_dict()
        # override the default output from pydantic by calling `to_dict()` of described_object
        if self.described_object:
            _dict['describedObject'] = self.described_object.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metric
        if self.metric:
            _dict['metric'] = self.metric.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V2ObjectMetricStatus:
        """Create an instance of V2ObjectMetricStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V2ObjectMetricStatus.parse_obj(obj)

        _obj = V2ObjectMetricStatus.parse_obj({
            "current": V2MetricValueStatus.from_dict(obj.get("current")) if obj.get("current") is not None else None,
            "described_object": V2CrossVersionObjectReference.from_dict(obj.get("describedObject")) if obj.get("describedObject") is not None else None,
            "metric": V2MetricIdentifier.from_dict(obj.get("metric")) if obj.get("metric") is not None else None
        })
        return _obj


