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
from .v1beta1_validating_admission_policy_binding_spec import V1beta1ValidatingAdmissionPolicyBindingSpec

class V1beta1ValidatingAdmissionPolicyBinding(BaseModel):
    """
    ValidatingAdmissionPolicyBinding binds the ValidatingAdmissionPolicy with paramerized resources. ValidatingAdmissionPolicyBinding and parameter CRDs together define how cluster administrators configure policies for clusters.  For a given admission request, each binding will cause its policy to be evaluated N times, where N is 1 for policies/bindings that don't use params, otherwise N is the number of parameters selected by the binding.  The CEL expressions of a policy must have a computed CEL cost below the maximum CEL budget. Each evaluation of the policy is given an independent CEL cost budget. Adding/removing policies, bindings, or params can not affect whether a given (policy, binding, param) combination is within its own CEL budget.  # noqa: E501
    """
    api_version: Optional[StrictStr] = Field(default=None, alias="apiVersion", description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources")
    kind: Optional[StrictStr] = Field(default=None, description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds")
    metadata: Optional[V1ObjectMeta] = None
    spec: Optional[V1beta1ValidatingAdmissionPolicyBindingSpec] = None
    __properties = ["apiVersion", "kind", "metadata", "spec"]

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
    def from_json(cls, json_str: str) -> V1beta1ValidatingAdmissionPolicyBinding:
        """Create an instance of V1beta1ValidatingAdmissionPolicyBinding from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1beta1ValidatingAdmissionPolicyBinding:
        """Create an instance of V1beta1ValidatingAdmissionPolicyBinding from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1beta1ValidatingAdmissionPolicyBinding.parse_obj(obj)

        _obj = V1beta1ValidatingAdmissionPolicyBinding.parse_obj({
            "api_version": obj.get("apiVersion"),
            "kind": obj.get("kind"),
            "metadata": V1ObjectMeta.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "spec": V1beta1ValidatingAdmissionPolicyBindingSpec.from_dict(obj.get("spec")) if obj.get("spec") is not None else None
        })
        return _obj


