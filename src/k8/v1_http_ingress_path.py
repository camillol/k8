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
from .v1_ingress_backend import V1IngressBackend

class V1HTTPIngressPath(BaseModel):
    """
    HTTPIngressPath associates a path with a backend. Incoming urls matching the path are forwarded to the backend.  # noqa: E501
    """
    backend: V1IngressBackend = Field(...)
    path: Optional[StrictStr] = Field(default=None, description="path is matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional \"path\" part of a URL as defined by RFC 3986. Paths must begin with a '/' and must be present when using PathType with value \"Exact\" or \"Prefix\".")
    path_type: StrictStr = Field(..., alias="pathType", description="pathType determines the interpretation of the path matching. PathType can be one of the following values: * Exact: Matches the URL path exactly. * Prefix: Matches based on a URL path prefix split by '/'. Matching is   done on a path element by element basis. A path element refers is the   list of labels in the path split by the '/' separator. A request is a   match for path p if every p is an element-wise prefix of p of the   request path. Note that if the last element of the path is a substring   of the last element in request path, it is not a match (e.g. /foo/bar   matches /foo/bar/baz, but does not match /foo/barbaz). * ImplementationSpecific: Interpretation of the Path matching is up to   the IngressClass. Implementations can treat this as a separate PathType   or treat it identically to Prefix or Exact path types. Implementations are required to support all path types.")
    __properties = ["backend", "path", "pathType"]

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
    def from_json(cls, json_str: str) -> V1HTTPIngressPath:
        """Create an instance of V1HTTPIngressPath from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of backend
        if self.backend:
            _dict['backend'] = self.backend.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1HTTPIngressPath:
        """Create an instance of V1HTTPIngressPath from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1HTTPIngressPath.parse_obj(obj)

        _obj = V1HTTPIngressPath.parse_obj({
            "backend": V1IngressBackend.from_dict(obj.get("backend")) if obj.get("backend") is not None else None,
            "path": obj.get("path"),
            "path_type": obj.get("pathType")
        })
        return _obj

