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
from pydantic import BaseModel, Field
from .v1_exec_action import V1ExecAction
from .v1_http_get_action import V1HTTPGetAction
from .v1_sleep_action import V1SleepAction
from .v1_tcp_socket_action import V1TCPSocketAction

class V1LifecycleHandler(BaseModel):
    """
    LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.  # noqa: E501
    """
    var_exec: Optional[V1ExecAction] = Field(default=None, alias="exec")
    http_get: Optional[V1HTTPGetAction] = Field(default=None, alias="httpGet")
    sleep: Optional[V1SleepAction] = None
    tcp_socket: Optional[V1TCPSocketAction] = Field(default=None, alias="tcpSocket")
    __properties = ["exec", "httpGet", "sleep", "tcpSocket"]

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
    def from_json(cls, json_str: str) -> V1LifecycleHandler:
        """Create an instance of V1LifecycleHandler from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_exec
        if self.var_exec:
            _dict['exec'] = self.var_exec.to_dict()
        # override the default output from pydantic by calling `to_dict()` of http_get
        if self.http_get:
            _dict['httpGet'] = self.http_get.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sleep
        if self.sleep:
            _dict['sleep'] = self.sleep.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tcp_socket
        if self.tcp_socket:
            _dict['tcpSocket'] = self.tcp_socket.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1LifecycleHandler:
        """Create an instance of V1LifecycleHandler from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1LifecycleHandler.parse_obj(obj)

        _obj = V1LifecycleHandler.parse_obj({
            "var_exec": V1ExecAction.from_dict(obj.get("exec")) if obj.get("exec") is not None else None,
            "http_get": V1HTTPGetAction.from_dict(obj.get("httpGet")) if obj.get("httpGet") is not None else None,
            "sleep": V1SleepAction.from_dict(obj.get("sleep")) if obj.get("sleep") is not None else None,
            "tcp_socket": V1TCPSocketAction.from_dict(obj.get("tcpSocket")) if obj.get("tcpSocket") is not None else None
        })
        return _obj

