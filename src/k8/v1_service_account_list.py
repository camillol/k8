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
from .v1_list_meta import V1ListMeta
from .v1_service_account import V1ServiceAccount

class V1ServiceAccountList(BaseModel):
    """
    ServiceAccountList is a list of ServiceAccount objects  # noqa: E501
    """
    api_version: Optional[StrictStr] = Field(default=None, alias="apiVersion", description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources")
    items: conlist(V1ServiceAccount) = Field(..., description="List of ServiceAccounts. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/")
    kind: Optional[StrictStr] = Field(default=None, description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds")
    metadata: Optional[V1ListMeta] = None
    __properties = ["apiVersion", "items", "kind", "metadata"]

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
    def from_json(cls, json_str: str) -> V1ServiceAccountList:
        """Create an instance of V1ServiceAccountList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ServiceAccountList:
        """Create an instance of V1ServiceAccountList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ServiceAccountList.parse_obj(obj)

        _obj = V1ServiceAccountList.parse_obj({
            "api_version": obj.get("apiVersion"),
            "items": [V1ServiceAccount.from_dict(_item) for _item in obj.get("items")] if obj.get("items") is not None else None,
            "kind": obj.get("kind"),
            "metadata": V1ListMeta.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None
        })
        return _obj


