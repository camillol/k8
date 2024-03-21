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


from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from .v1_local_object_reference import V1LocalObjectReference

class V1FlexVolumeSource(BaseModel):
    """
    FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.  # noqa: E501
    """
    driver: StrictStr = Field(..., description="driver is the name of the driver to use for this volume.")
    fs_type: Optional[StrictStr] = Field(default=None, alias="fsType", description="fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". The default filesystem depends on FlexVolume script.")
    options: Optional[Dict[str, StrictStr]] = Field(default=None, description="options is Optional: this field holds extra command options if any.")
    read_only: Optional[StrictBool] = Field(default=None, alias="readOnly", description="readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.")
    secret_ref: Optional[V1LocalObjectReference] = Field(default=None, alias="secretRef")
    __properties = ["driver", "fsType", "options", "readOnly", "secretRef"]

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
    def from_json(cls, json_str: str) -> V1FlexVolumeSource:
        """Create an instance of V1FlexVolumeSource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of secret_ref
        if self.secret_ref:
            _dict['secretRef'] = self.secret_ref.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1FlexVolumeSource:
        """Create an instance of V1FlexVolumeSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1FlexVolumeSource.parse_obj(obj)

        _obj = V1FlexVolumeSource.parse_obj({
            "driver": obj.get("driver"),
            "fs_type": obj.get("fsType"),
            "options": obj.get("options"),
            "read_only": obj.get("readOnly"),
            "secret_ref": V1LocalObjectReference.from_dict(obj.get("secretRef")) if obj.get("secretRef") is not None else None
        })
        return _obj


