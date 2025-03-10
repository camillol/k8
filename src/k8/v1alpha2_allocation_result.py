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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from .v1_node_selector import V1NodeSelector
from .v1alpha2_resource_handle import V1alpha2ResourceHandle
from typing import Optional, Set
from typing_extensions import Self

class V1alpha2AllocationResult(BaseModel):
    """
    AllocationResult contains attributes of an allocated resource.
    """ # noqa: E501
    available_on_nodes: Optional[V1NodeSelector] = Field(default=None, alias="availableOnNodes")
    resource_handles: Optional[List[V1alpha2ResourceHandle]] = Field(default=None, description="ResourceHandles contain the state associated with an allocation that should be maintained throughout the lifetime of a claim. Each ResourceHandle contains data that should be passed to a specific kubelet plugin once it lands on a node. This data is returned by the driver after a successful allocation and is opaque to Kubernetes. Driver documentation may explain to users how to interpret this data if needed.  Setting this field is optional. It has a maximum size of 32 entries. If null (or empty), it is assumed this allocation will be processed by a single kubelet plugin with no ResourceHandle data attached. The name of the kubelet plugin invoked will match the DriverName set in the ResourceClaimStatus this AllocationResult is embedded in.", alias="resourceHandles")
    shareable: Optional[StrictBool] = Field(default=None, description="Shareable determines whether the resource supports more than one consumer at a time.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["availableOnNodes", "resourceHandles", "shareable"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V1alpha2AllocationResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of available_on_nodes
        if self.available_on_nodes:
            _dict['availableOnNodes'] = self.available_on_nodes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in resource_handles (list)
        _items = []
        if self.resource_handles:
            for _item in self.resource_handles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['resourceHandles'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1alpha2AllocationResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availableOnNodes": V1NodeSelector.from_dict(obj["availableOnNodes"]) if obj.get("availableOnNodes") is not None else None,
            "resourceHandles": [V1alpha2ResourceHandle.from_dict(_item) for _item in obj["resourceHandles"]] if obj.get("resourceHandles") is not None else None,
            "shareable": obj.get("shareable")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


