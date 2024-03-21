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
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from .events_v1_event_series import EventsV1EventSeries
from .v1_event_source import V1EventSource
from .v1_object_meta import V1ObjectMeta
from .v1_object_reference import V1ObjectReference

class EventsV1Event(BaseModel):
    """
    Event is a report of an event somewhere in the cluster. It generally denotes some state change in the system. Events have a limited retention time and triggers and messages may evolve with time.  Event consumers should not rely on the timing of an event with a given Reason reflecting a consistent underlying trigger, or the continued existence of events with that Reason.  Events should be treated as informative, best-effort, supplemental data.  # noqa: E501
    """
    action: Optional[StrictStr] = Field(default=None, description="action is what action was taken/failed regarding to the regarding object. It is machine-readable. This field cannot be empty for new Events and it can have at most 128 characters.")
    api_version: Optional[StrictStr] = Field(default=None, alias="apiVersion", description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources")
    deprecated_count: Optional[StrictInt] = Field(default=None, alias="deprecatedCount", description="deprecatedCount is the deprecated field assuring backward compatibility with core.v1 Event type.")
    deprecated_first_timestamp: Optional[datetime] = Field(default=None, alias="deprecatedFirstTimestamp", description="deprecatedFirstTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.")
    deprecated_last_timestamp: Optional[datetime] = Field(default=None, alias="deprecatedLastTimestamp", description="deprecatedLastTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.")
    deprecated_source: Optional[V1EventSource] = Field(default=None, alias="deprecatedSource")
    event_time: datetime = Field(..., alias="eventTime", description="eventTime is the time when this Event was first observed. It is required.")
    kind: Optional[StrictStr] = Field(default=None, description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds")
    metadata: Optional[V1ObjectMeta] = None
    note: Optional[StrictStr] = Field(default=None, description="note is a human-readable description of the status of this operation. Maximal length of the note is 1kB, but libraries should be prepared to handle values up to 64kB.")
    reason: Optional[StrictStr] = Field(default=None, description="reason is why the action was taken. It is human-readable. This field cannot be empty for new Events and it can have at most 128 characters.")
    regarding: Optional[V1ObjectReference] = None
    related: Optional[V1ObjectReference] = None
    reporting_controller: Optional[StrictStr] = Field(default=None, alias="reportingController", description="reportingController is the name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`. This field cannot be empty for new Events.")
    reporting_instance: Optional[StrictStr] = Field(default=None, alias="reportingInstance", description="reportingInstance is the ID of the controller instance, e.g. `kubelet-xyzf`. This field cannot be empty for new Events and it can have at most 128 characters.")
    series: Optional[EventsV1EventSeries] = None
    type: Optional[StrictStr] = Field(default=None, description="type is the type of this event (Normal, Warning), new types could be added in the future. It is machine-readable. This field cannot be empty for new Events.")
    __properties = ["action", "apiVersion", "deprecatedCount", "deprecatedFirstTimestamp", "deprecatedLastTimestamp", "deprecatedSource", "eventTime", "kind", "metadata", "note", "reason", "regarding", "related", "reportingController", "reportingInstance", "series", "type"]

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
    def from_json(cls, json_str: str) -> EventsV1Event:
        """Create an instance of EventsV1Event from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of deprecated_source
        if self.deprecated_source:
            _dict['deprecatedSource'] = self.deprecated_source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of regarding
        if self.regarding:
            _dict['regarding'] = self.regarding.to_dict()
        # override the default output from pydantic by calling `to_dict()` of related
        if self.related:
            _dict['related'] = self.related.to_dict()
        # override the default output from pydantic by calling `to_dict()` of series
        if self.series:
            _dict['series'] = self.series.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventsV1Event:
        """Create an instance of EventsV1Event from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EventsV1Event.parse_obj(obj)

        _obj = EventsV1Event.parse_obj({
            "action": obj.get("action"),
            "api_version": obj.get("apiVersion"),
            "deprecated_count": obj.get("deprecatedCount"),
            "deprecated_first_timestamp": obj.get("deprecatedFirstTimestamp"),
            "deprecated_last_timestamp": obj.get("deprecatedLastTimestamp"),
            "deprecated_source": V1EventSource.from_dict(obj.get("deprecatedSource")) if obj.get("deprecatedSource") is not None else None,
            "event_time": obj.get("eventTime"),
            "kind": obj.get("kind"),
            "metadata": V1ObjectMeta.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "note": obj.get("note"),
            "reason": obj.get("reason"),
            "regarding": V1ObjectReference.from_dict(obj.get("regarding")) if obj.get("regarding") is not None else None,
            "related": V1ObjectReference.from_dict(obj.get("related")) if obj.get("related") is not None else None,
            "reporting_controller": obj.get("reportingController"),
            "reporting_instance": obj.get("reportingInstance"),
            "series": EventsV1EventSeries.from_dict(obj.get("series")) if obj.get("series") is not None else None,
            "type": obj.get("type")
        })
        return _obj


