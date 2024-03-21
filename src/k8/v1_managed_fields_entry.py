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

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr

class V1ManagedFieldsEntry(BaseModel):
    """
    ManagedFieldsEntry is a workflow-id, a FieldSet and the group version of the resource that the fieldset applies to.  # noqa: E501
    """
    api_version: Optional[StrictStr] = Field(default=None, alias="apiVersion", description="APIVersion defines the version of this resource that this field set applies to. The format is \"group/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted.")
    fields_type: Optional[StrictStr] = Field(default=None, alias="fieldsType", description="FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: \"FieldsV1\"")
    fields_v1: Optional[Dict[str, Any]] = Field(default=None, alias="fieldsV1", description="FieldsV1 holds the first JSON version format as described in the \"FieldsV1\" type.")
    manager: Optional[StrictStr] = Field(default=None, description="Manager is an identifier of the workflow managing these fields.")
    operation: Optional[StrictStr] = Field(default=None, description="Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'.")
    subresource: Optional[StrictStr] = Field(default=None, description="Subresource is the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource.")
    time: Optional[datetime] = Field(default=None, description="Time is the timestamp of when the ManagedFields entry was added. The timestamp will also be updated if a field is added, the manager changes any of the owned fields value or removes a field. The timestamp does not update when a field is removed from the entry because another manager took it over.")
    __properties = ["apiVersion", "fieldsType", "fieldsV1", "manager", "operation", "subresource", "time"]

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
    def from_json(cls, json_str: str) -> V1ManagedFieldsEntry:
        """Create an instance of V1ManagedFieldsEntry from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ManagedFieldsEntry:
        """Create an instance of V1ManagedFieldsEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ManagedFieldsEntry.parse_obj(obj)

        _obj = V1ManagedFieldsEntry.parse_obj({
            "api_version": obj.get("apiVersion"),
            "fields_type": obj.get("fieldsType"),
            "fields_v1": obj.get("fieldsV1"),
            "manager": obj.get("manager"),
            "operation": obj.get("operation"),
            "subresource": obj.get("subresource"),
            "time": obj.get("time")
        })
        return _obj


