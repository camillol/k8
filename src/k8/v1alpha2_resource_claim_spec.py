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
from .v1alpha2_resource_claim_parameters_reference import V1alpha2ResourceClaimParametersReference

class V1alpha2ResourceClaimSpec(BaseModel):
    """
    ResourceClaimSpec defines how a resource is to be allocated.  # noqa: E501
    """
    allocation_mode: Optional[StrictStr] = Field(default=None, alias="allocationMode", description="Allocation can start immediately or when a Pod wants to use the resource. \"WaitForFirstConsumer\" is the default.")
    parameters_ref: Optional[V1alpha2ResourceClaimParametersReference] = Field(default=None, alias="parametersRef")
    resource_class_name: StrictStr = Field(..., alias="resourceClassName", description="ResourceClassName references the driver and additional parameters via the name of a ResourceClass that was created as part of the driver deployment.")
    __properties = ["allocationMode", "parametersRef", "resourceClassName"]

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
    def from_json(cls, json_str: str) -> V1alpha2ResourceClaimSpec:
        """Create an instance of V1alpha2ResourceClaimSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of parameters_ref
        if self.parameters_ref:
            _dict['parametersRef'] = self.parameters_ref.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1alpha2ResourceClaimSpec:
        """Create an instance of V1alpha2ResourceClaimSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1alpha2ResourceClaimSpec.parse_obj(obj)

        _obj = V1alpha2ResourceClaimSpec.parse_obj({
            "allocation_mode": obj.get("allocationMode"),
            "parameters_ref": V1alpha2ResourceClaimParametersReference.from_dict(obj.get("parametersRef")) if obj.get("parametersRef") is not None else None,
            "resource_class_name": obj.get("resourceClassName")
        })
        return _obj


