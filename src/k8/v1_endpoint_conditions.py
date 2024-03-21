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
from pydantic import BaseModel, Field, StrictBool

class V1EndpointConditions(BaseModel):
    """
    EndpointConditions represents the current condition of an endpoint.  # noqa: E501
    """
    ready: Optional[StrictBool] = Field(default=None, description="ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should interpret this unknown state as ready. For compatibility reasons, ready should never be \"true\" for terminating endpoints, except when the normal readiness behavior is being explicitly overridden, for example when the associated Service has set the publishNotReadyAddresses flag.")
    serving: Optional[StrictBool] = Field(default=None, description="serving is identical to ready except that it is set regardless of the terminating state of endpoints. This condition should be set to true for a ready endpoint that is terminating. If nil, consumers should defer to the ready condition.")
    terminating: Optional[StrictBool] = Field(default=None, description="terminating indicates that this endpoint is terminating. A nil value indicates an unknown state. Consumers should interpret this unknown state to mean that the endpoint is not terminating.")
    __properties = ["ready", "serving", "terminating"]

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
    def from_json(cls, json_str: str) -> V1EndpointConditions:
        """Create an instance of V1EndpointConditions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1EndpointConditions:
        """Create an instance of V1EndpointConditions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1EndpointConditions.parse_obj(obj)

        _obj = V1EndpointConditions.parse_obj({
            "ready": obj.get("ready"),
            "serving": obj.get("serving"),
            "terminating": obj.get("terminating")
        })
        return _obj

