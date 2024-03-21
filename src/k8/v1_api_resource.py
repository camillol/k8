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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist

class V1APIResource(BaseModel):
    """
    APIResource specifies the name of a resource and whether it is namespaced.  # noqa: E501
    """
    categories: Optional[conlist(StrictStr)] = Field(default=None, description="categories is a list of the grouped resources this resource belongs to (e.g. 'all')")
    group: Optional[StrictStr] = Field(default=None, description="group is the preferred group of the resource.  Empty implies the group of the containing resource list. For subresources, this may have a different value, for example: Scale\".")
    kind: StrictStr = Field(..., description="kind is the kind for the resource (e.g. 'Foo' is the kind for a resource 'foo')")
    name: StrictStr = Field(..., description="name is the plural name of the resource.")
    namespaced: StrictBool = Field(..., description="namespaced indicates if a resource is namespaced or not.")
    short_names: Optional[conlist(StrictStr)] = Field(default=None, alias="shortNames", description="shortNames is a list of suggested short names of the resource.")
    singular_name: StrictStr = Field(..., alias="singularName", description="singularName is the singular name of the resource.  This allows clients to handle plural and singular opaquely. The singularName is more correct for reporting status on a single item and both singular and plural are allowed from the kubectl CLI interface.")
    storage_version_hash: Optional[StrictStr] = Field(default=None, alias="storageVersionHash", description="The hash value of the storage version, the version this resource is converted to when written to the data store. Value must be treated as opaque by clients. Only equality comparison on the value is valid. This is an alpha feature and may change or be removed in the future. The field is populated by the apiserver only if the StorageVersionHash feature gate is enabled. This field will remain optional even if it graduates.")
    verbs: conlist(StrictStr) = Field(..., description="verbs is a list of supported kube verbs (this includes get, list, watch, create, update, patch, delete, deletecollection, and proxy)")
    version: Optional[StrictStr] = Field(default=None, description="version is the preferred version of the resource.  Empty implies the version of the containing resource list For subresources, this may have a different value, for example: v1 (while inside a v1beta1 version of the core resource's group)\".")
    __properties = ["categories", "group", "kind", "name", "namespaced", "shortNames", "singularName", "storageVersionHash", "verbs", "version"]

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
    def from_json(cls, json_str: str) -> V1APIResource:
        """Create an instance of V1APIResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1APIResource:
        """Create an instance of V1APIResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1APIResource.parse_obj(obj)

        _obj = V1APIResource.parse_obj({
            "categories": obj.get("categories"),
            "group": obj.get("group"),
            "kind": obj.get("kind"),
            "name": obj.get("name"),
            "namespaced": obj.get("namespaced"),
            "short_names": obj.get("shortNames"),
            "singular_name": obj.get("singularName"),
            "storage_version_hash": obj.get("storageVersionHash"),
            "verbs": obj.get("verbs"),
            "version": obj.get("version")
        })
        return _obj


