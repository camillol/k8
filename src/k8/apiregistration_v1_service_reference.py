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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class ApiregistrationV1ServiceReference(BaseModel):
    """
    ServiceReference holds a reference to Service.legacy.k8s.io  # noqa: E501
    """
    name: Optional[StrictStr] = Field(default=None, description="Name is the name of the service")
    namespace: Optional[StrictStr] = Field(default=None, description="Namespace is the namespace of the service")
    port: Optional[StrictInt] = Field(default=None, description="If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. `port` should be a valid port number (1-65535, inclusive).")
    __properties = ["name", "namespace", "port"]

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
    def from_json(cls, json_str: str) -> ApiregistrationV1ServiceReference:
        """Create an instance of ApiregistrationV1ServiceReference from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiregistrationV1ServiceReference:
        """Create an instance of ApiregistrationV1ServiceReference from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiregistrationV1ServiceReference.parse_obj(obj)

        _obj = ApiregistrationV1ServiceReference.parse_obj({
            "name": obj.get("name"),
            "namespace": obj.get("namespace"),
            "port": obj.get("port")
        })
        return _obj


