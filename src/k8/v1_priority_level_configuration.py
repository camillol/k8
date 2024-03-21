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
from pydantic import BaseModel, Field, StrictStr
from .v1_object_meta import V1ObjectMeta
from .v1_priority_level_configuration_spec import V1PriorityLevelConfigurationSpec
from .v1_priority_level_configuration_status import V1PriorityLevelConfigurationStatus

class V1PriorityLevelConfiguration(BaseModel):
    """
    PriorityLevelConfiguration represents the configuration of a priority level.  # noqa: E501
    """
    api_version: Optional[StrictStr] = Field(default=None, alias="apiVersion", description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources")
    kind: Optional[StrictStr] = Field(default=None, description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds")
    metadata: Optional[V1ObjectMeta] = None
    spec: Optional[V1PriorityLevelConfigurationSpec] = None
    status: Optional[V1PriorityLevelConfigurationStatus] = None
    __properties = ["apiVersion", "kind", "metadata", "spec", "status"]

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
    def from_json(cls, json_str: str) -> V1PriorityLevelConfiguration:
        """Create an instance of V1PriorityLevelConfiguration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spec
        if self.spec:
            _dict['spec'] = self.spec.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1PriorityLevelConfiguration:
        """Create an instance of V1PriorityLevelConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1PriorityLevelConfiguration.parse_obj(obj)

        _obj = V1PriorityLevelConfiguration.parse_obj({
            "api_version": obj.get("apiVersion"),
            "kind": obj.get("kind"),
            "metadata": V1ObjectMeta.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "spec": V1PriorityLevelConfigurationSpec.from_dict(obj.get("spec")) if obj.get("spec") is not None else None,
            "status": V1PriorityLevelConfigurationStatus.from_dict(obj.get("status")) if obj.get("status") is not None else None
        })
        return _obj


