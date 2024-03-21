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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class V1WindowsSecurityContextOptions(BaseModel):
    """
    WindowsSecurityContextOptions contain Windows-specific options and credentials.  # noqa: E501
    """
    gmsa_credential_spec: Optional[StrictStr] = Field(default=None, alias="gmsaCredentialSpec", description="GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field.")
    gmsa_credential_spec_name: Optional[StrictStr] = Field(default=None, alias="gmsaCredentialSpecName", description="GMSACredentialSpecName is the name of the GMSA credential spec to use.")
    host_process: Optional[StrictBool] = Field(default=None, alias="hostProcess", description="HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod's containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true.")
    run_as_user_name: Optional[StrictStr] = Field(default=None, alias="runAsUserName", description="The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.")
    __properties = ["gmsaCredentialSpec", "gmsaCredentialSpecName", "hostProcess", "runAsUserName"]

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
    def from_json(cls, json_str: str) -> V1WindowsSecurityContextOptions:
        """Create an instance of V1WindowsSecurityContextOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1WindowsSecurityContextOptions:
        """Create an instance of V1WindowsSecurityContextOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1WindowsSecurityContextOptions.parse_obj(obj)

        _obj = V1WindowsSecurityContextOptions.parse_obj({
            "gmsa_credential_spec": obj.get("gmsaCredentialSpec"),
            "gmsa_credential_spec_name": obj.get("gmsaCredentialSpecName"),
            "host_process": obj.get("hostProcess"),
            "run_as_user_name": obj.get("runAsUserName")
        })
        return _obj

