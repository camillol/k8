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


from typing import Dict, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictStr, conbytes, constr, validator
from .v1_object_meta import V1ObjectMeta

class V1Secret(BaseModel):
    """
    Secret holds secret data of a certain type. The total bytes of the values in the Data field must be less than MaxSecretSize bytes.  # noqa: E501
    """
    api_version: Optional[StrictStr] = Field(default=None, alias="apiVersion", description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources")
    data: Optional[Dict[str, Union[conbytes(strict=True), constr(strict=True)]]] = Field(default=None, description="Data contains the secret data. Each key must consist of alphanumeric characters, '-', '_' or '.'. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here. Described in https://tools.ietf.org/html/rfc4648#section-4")
    immutable: Optional[StrictBool] = Field(default=None, description="Immutable, if set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil.")
    kind: Optional[StrictStr] = Field(default=None, description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds")
    metadata: Optional[V1ObjectMeta] = None
    string_data: Optional[Dict[str, StrictStr]] = Field(default=None, alias="stringData", description="stringData allows specifying non-binary secret data in string form. It is provided as a write-only input field for convenience. All keys and values are merged into the data field on write, overwriting any existing values. The stringData field is never output when reading from the API.")
    type: Optional[StrictStr] = Field(default=None, description="Used to facilitate programmatic handling of secret data. More info: https://kubernetes.io/docs/concepts/configuration/secret/#secret-types")
    __properties = ["apiVersion", "data", "immutable", "kind", "metadata", "stringData", "type"]

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
    def from_json(cls, json_str: str) -> V1Secret:
        """Create an instance of V1Secret from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1Secret:
        """Create an instance of V1Secret from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1Secret.parse_obj(obj)

        _obj = V1Secret.parse_obj({
            "api_version": obj.get("apiVersion"),
            "data": obj.get("data"),
            "immutable": obj.get("immutable"),
            "kind": obj.get("kind"),
            "metadata": V1ObjectMeta.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "string_data": obj.get("stringData"),
            "type": obj.get("type")
        })
        return _obj


