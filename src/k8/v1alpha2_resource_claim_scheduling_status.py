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

class V1alpha2ResourceClaimSchedulingStatus(BaseModel):
    """
    ResourceClaimSchedulingStatus contains information about one particular ResourceClaim with \"WaitForFirstConsumer\" allocation mode.  # noqa: E501
    """
    name: Optional[StrictStr] = Field(default=None, description="Name matches the pod.spec.resourceClaims[*].Name field.")
    unsuitable_nodes: Optional[conlist(StrictStr)] = Field(default=None, alias="unsuitableNodes", description="UnsuitableNodes lists nodes that the ResourceClaim cannot be allocated for.  The size of this field is limited to 128, the same as for PodSchedulingSpec.PotentialNodes. This may get increased in the future, but not reduced.")
    __properties = ["name", "unsuitableNodes"]

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
    def from_json(cls, json_str: str) -> V1alpha2ResourceClaimSchedulingStatus:
        """Create an instance of V1alpha2ResourceClaimSchedulingStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1alpha2ResourceClaimSchedulingStatus:
        """Create an instance of V1alpha2ResourceClaimSchedulingStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1alpha2ResourceClaimSchedulingStatus.parse_obj(obj)

        _obj = V1alpha2ResourceClaimSchedulingStatus.parse_obj({
            "name": obj.get("name"),
            "unsuitable_nodes": obj.get("unsuitableNodes")
        })
        return _obj


