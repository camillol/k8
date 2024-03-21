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

class DiscoveryV1EndpointPort(BaseModel):
    """
    EndpointPort represents a Port used by an EndpointSlice  # noqa: E501
    """
    app_protocol: Optional[StrictStr] = Field(default=None, alias="appProtocol", description="The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. This field follows standard Kubernetes label syntax. Valid values are either:  * Un-prefixed protocol names - reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).  * Kubernetes-defined prefixed names:   * 'kubernetes.io/h2c' - HTTP/2 prior knowledge over cleartext as described in https://www.rfc-editor.org/rfc/rfc9113.html#name-starting-http-2-with-prior-   * 'kubernetes.io/ws'  - WebSocket over cleartext as described in https://www.rfc-editor.org/rfc/rfc6455   * 'kubernetes.io/wss' - WebSocket over TLS as described in https://www.rfc-editor.org/rfc/rfc6455  * Other protocols should use implementation-defined prefixed names such as mycompany.com/my-custom-protocol.")
    name: Optional[StrictStr] = Field(default=None, description="name represents the name of this port. All ports in an EndpointSlice must have a unique name. If the EndpointSlice is derived from a Kubernetes service, this corresponds to the Service.ports[].name. Name must either be an empty string or pass DNS_LABEL validation: * must be no more than 63 characters long. * must consist of lower case alphanumeric characters or '-'. * must start and end with an alphanumeric character. Default is empty string.")
    port: Optional[StrictInt] = Field(default=None, description="port represents the port number of the endpoint. If this is not specified, ports are not restricted and must be interpreted in the context of the specific consumer.")
    protocol: Optional[StrictStr] = Field(default=None, description="protocol represents the IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.")
    __properties = ["appProtocol", "name", "port", "protocol"]

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
    def from_json(cls, json_str: str) -> DiscoveryV1EndpointPort:
        """Create an instance of DiscoveryV1EndpointPort from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DiscoveryV1EndpointPort:
        """Create an instance of DiscoveryV1EndpointPort from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DiscoveryV1EndpointPort.parse_obj(obj)

        _obj = DiscoveryV1EndpointPort.parse_obj({
            "app_protocol": obj.get("appProtocol"),
            "name": obj.get("name"),
            "port": obj.get("port"),
            "protocol": obj.get("protocol")
        })
        return _obj


