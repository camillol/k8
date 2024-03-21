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

class V1EmptyDirVolumeSource(BaseModel):
    """
    Represents an empty directory for a pod. Empty directory volumes support ownership management and SELinux relabeling.  # noqa: E501
    """
    medium: Optional[StrictStr] = Field(default=None, description="medium represents what type of storage medium should back this directory. The default is \"\" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir")
    size_limit: Optional[StrictStr] = Field(default=None, alias="sizeLimit", description="sizeLimit is the total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir")
    __properties = ["medium", "sizeLimit"]

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
    def from_json(cls, json_str: str) -> V1EmptyDirVolumeSource:
        """Create an instance of V1EmptyDirVolumeSource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1EmptyDirVolumeSource:
        """Create an instance of V1EmptyDirVolumeSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1EmptyDirVolumeSource.parse_obj(obj)

        _obj = V1EmptyDirVolumeSource.parse_obj({
            "medium": obj.get("medium"),
            "size_limit": obj.get("sizeLimit")
        })
        return _obj


