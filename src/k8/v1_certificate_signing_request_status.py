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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, conbytes, conlist, constr, validator
from .v1_certificate_signing_request_condition import V1CertificateSigningRequestCondition

class V1CertificateSigningRequestStatus(BaseModel):
    """
    CertificateSigningRequestStatus contains conditions used to indicate approved/denied/failed status of the request, and the issued certificate.  # noqa: E501
    """
    certificate: Optional[Union[conbytes(strict=True), constr(strict=True)]] = Field(default=None, description="certificate is populated with an issued certificate by the signer after an Approved condition is present. This field is set via the /status subresource. Once populated, this field is immutable.  If the certificate signing request is denied, a condition of type \"Denied\" is added and this field remains empty. If the signer cannot issue the certificate, a condition of type \"Failed\" is added and this field remains empty.  Validation requirements:  1. certificate must contain one or more PEM blocks.  2. All PEM blocks must have the \"CERTIFICATE\" label, contain no headers, and the encoded data   must be a BER-encoded ASN.1 Certificate structure as described in section 4 of RFC5280.  3. Non-PEM content may appear before or after the \"CERTIFICATE\" PEM blocks and is unvalidated,   to allow for explanatory text as described in section 5.2 of RFC7468.  If more than one PEM block is present, and the definition of the requested spec.signerName does not indicate otherwise, the first block is the issued certificate, and subsequent blocks should be treated as intermediate certificates and presented in TLS handshakes.  The certificate is encoded in PEM format.  When serialized as JSON or YAML, the data is additionally base64-encoded, so it consists of:      base64(     -----BEGIN CERTIFICATE-----     ...     -----END CERTIFICATE-----     )")
    conditions: Optional[conlist(V1CertificateSigningRequestCondition)] = Field(default=None, description="conditions applied to the request. Known conditions are \"Approved\", \"Denied\", and \"Failed\".")
    __properties = ["certificate", "conditions"]

    @validator('certificate')
    def certificate_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$", value):
            raise ValueError(r"must validate the regular expression /^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/")
        return value

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
    def from_json(cls, json_str: str) -> V1CertificateSigningRequestStatus:
        """Create an instance of V1CertificateSigningRequestStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in conditions (list)
        _items = []
        if self.conditions:
            for _item in self.conditions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['conditions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1CertificateSigningRequestStatus:
        """Create an instance of V1CertificateSigningRequestStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1CertificateSigningRequestStatus.parse_obj(obj)

        _obj = V1CertificateSigningRequestStatus.parse_obj({
            "certificate": obj.get("certificate"),
            "conditions": [V1CertificateSigningRequestCondition.from_dict(_item) for _item in obj.get("conditions")] if obj.get("conditions") is not None else None
        })
        return _obj


