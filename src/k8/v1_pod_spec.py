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


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from .v1_affinity import V1Affinity
from .v1_container import V1Container
from .v1_ephemeral_container import V1EphemeralContainer
from .v1_host_alias import V1HostAlias
from .v1_local_object_reference import V1LocalObjectReference
from .v1_pod_dns_config import V1PodDNSConfig
from .v1_pod_os import V1PodOS
from .v1_pod_readiness_gate import V1PodReadinessGate
from .v1_pod_resource_claim import V1PodResourceClaim
from .v1_pod_scheduling_gate import V1PodSchedulingGate
from .v1_pod_security_context import V1PodSecurityContext
from .v1_toleration import V1Toleration
from .v1_topology_spread_constraint import V1TopologySpreadConstraint
from .v1_volume import V1Volume

class V1PodSpec(BaseModel):
    """
    PodSpec is a description of a pod.  # noqa: E501
    """
    active_deadline_seconds: Optional[StrictInt] = Field(default=None, alias="activeDeadlineSeconds", description="Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.")
    affinity: Optional[V1Affinity] = None
    automount_service_account_token: Optional[StrictBool] = Field(default=None, alias="automountServiceAccountToken", description="AutomountServiceAccountToken indicates whether a service account token should be automatically mounted.")
    containers: conlist(V1Container) = Field(..., description="List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated.")
    dns_config: Optional[V1PodDNSConfig] = Field(default=None, alias="dnsConfig")
    dns_policy: Optional[StrictStr] = Field(default=None, alias="dnsPolicy", description="Set DNS policy for the pod. Defaults to \"ClusterFirst\". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.")
    enable_service_links: Optional[StrictBool] = Field(default=None, alias="enableServiceLinks", description="EnableServiceLinks indicates whether information about services should be injected into pod's environment variables, matching the syntax of Docker links. Optional: Defaults to true.")
    ephemeral_containers: Optional[conlist(V1EphemeralContainer)] = Field(default=None, alias="ephemeralContainers", description="List of ephemeral containers run in this pod. Ephemeral containers may be run in an existing pod to perform user-initiated actions such as debugging. This list cannot be specified when creating a pod, and it cannot be modified by updating the pod spec. In order to add an ephemeral container to an existing pod, use the pod's ephemeralcontainers subresource.")
    host_aliases: Optional[conlist(V1HostAlias)] = Field(default=None, alias="hostAliases", description="HostAliases is an optional list of hosts and IPs that will be injected into the pod's hosts file if specified. This is only valid for non-hostNetwork pods.")
    host_ipc: Optional[StrictBool] = Field(default=None, alias="hostIPC", description="Use the host's ipc namespace. Optional: Default to false.")
    host_network: Optional[StrictBool] = Field(default=None, alias="hostNetwork", description="Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false.")
    host_pid: Optional[StrictBool] = Field(default=None, alias="hostPID", description="Use the host's pid namespace. Optional: Default to false.")
    host_users: Optional[StrictBool] = Field(default=None, alias="hostUsers", description="Use the host's user namespace. Optional: Default to true. If set to true or not present, the pod will be run in the host user namespace, useful for when the pod needs a feature only available to the host user namespace, such as loading a kernel module with CAP_SYS_MODULE. When set to false, a new userns is created for the pod. Setting false is useful for mitigating container breakout vulnerabilities even allowing users to run their containers as root without actually having root privileges on the host. This field is alpha-level and is only honored by servers that enable the UserNamespacesSupport feature.")
    hostname: Optional[StrictStr] = Field(default=None, description="Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value.")
    image_pull_secrets: Optional[conlist(V1LocalObjectReference)] = Field(default=None, alias="imagePullSecrets", description="ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. More info: https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod")
    init_containers: Optional[conlist(V1Container)] = Field(default=None, alias="initContainers", description="List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added or removed. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/")
    node_name: Optional[StrictStr] = Field(default=None, alias="nodeName", description="NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements.")
    node_selector: Optional[Dict[str, StrictStr]] = Field(default=None, alias="nodeSelector", description="NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/")
    os: Optional[V1PodOS] = None
    overhead: Optional[Dict[str, StrictStr]] = Field(default=None, description="Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. This field will be autopopulated at admission time by the RuntimeClass admission controller. If the RuntimeClass admission controller is enabled, overhead must not be set in Pod create requests. The RuntimeClass admission controller will reject Pod create requests which have the overhead already set. If RuntimeClass is configured and selected in the PodSpec, Overhead will be set to the value defined in the corresponding RuntimeClass, otherwise it will remain unset and treated as zero. More info: https://git.k8s.io/enhancements/keps/sig-node/688-pod-overhead/README.md")
    preemption_policy: Optional[StrictStr] = Field(default=None, alias="preemptionPolicy", description="PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset.")
    priority: Optional[StrictInt] = Field(default=None, description="The priority value. Various system components use this field to find the priority of the pod. When Priority Admission Controller is enabled, it prevents users from setting this field. The admission controller populates this field from PriorityClassName. The higher the value, the higher the priority.")
    priority_class_name: Optional[StrictStr] = Field(default=None, alias="priorityClassName", description="If specified, indicates the pod's priority. \"system-node-critical\" and \"system-cluster-critical\" are two special keywords which indicate the highest priorities with the former being the highest priority. Any other name must be defined by creating a PriorityClass object with that name. If not specified, the pod priority will be default or zero if there is no default.")
    readiness_gates: Optional[conlist(V1PodReadinessGate)] = Field(default=None, alias="readinessGates", description="If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to \"True\" More info: https://git.k8s.io/enhancements/keps/sig-network/580-pod-readiness-gates")
    resource_claims: Optional[conlist(V1PodResourceClaim)] = Field(default=None, alias="resourceClaims", description="ResourceClaims defines which ResourceClaims must be allocated and reserved before the Pod is allowed to start. The resources will be made available to those containers which consume them by name.  This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.  This field is immutable.")
    restart_policy: Optional[StrictStr] = Field(default=None, alias="restartPolicy", description="Restart policy for all containers within the pod. One of Always, OnFailure, Never. In some contexts, only a subset of those values may be permitted. Default to Always. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy")
    runtime_class_name: Optional[StrictStr] = Field(default=None, alias="runtimeClassName", description="RuntimeClassName refers to a RuntimeClass object in the node.k8s.io group, which should be used to run this pod.  If no RuntimeClass resource matches the named class, the pod will not be run. If unset or empty, the \"legacy\" RuntimeClass will be used, which is an implicit class with an empty definition that uses the default runtime handler. More info: https://git.k8s.io/enhancements/keps/sig-node/585-runtime-class")
    scheduler_name: Optional[StrictStr] = Field(default=None, alias="schedulerName", description="If specified, the pod will be dispatched by specified scheduler. If not specified, the pod will be dispatched by default scheduler.")
    scheduling_gates: Optional[conlist(V1PodSchedulingGate)] = Field(default=None, alias="schedulingGates", description="SchedulingGates is an opaque list of values that if specified will block scheduling the pod. If schedulingGates is not empty, the pod will stay in the SchedulingGated state and the scheduler will not attempt to schedule the pod.  SchedulingGates can only be set at pod creation time, and be removed only afterwards.  This is a beta feature enabled by the PodSchedulingReadiness feature gate.")
    security_context: Optional[V1PodSecurityContext] = Field(default=None, alias="securityContext")
    service_account: Optional[StrictStr] = Field(default=None, alias="serviceAccount", description="DeprecatedServiceAccount is a depreciated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.")
    service_account_name: Optional[StrictStr] = Field(default=None, alias="serviceAccountName", description="ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/")
    set_hostname_as_fqdn: Optional[StrictBool] = Field(default=None, alias="setHostnameAsFQDN", description="If true the pod's hostname will be configured as the pod's FQDN, rather than the leaf name (the default). In Linux containers, this means setting the FQDN in the hostname field of the kernel (the nodename field of struct utsname). In Windows containers, this means setting the registry value of hostname for the registry key HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters to FQDN. If a pod does not have FQDN, this has no effect. Default to false.")
    share_process_namespace: Optional[StrictBool] = Field(default=None, alias="shareProcessNamespace", description="Share a single process namespace between all of the containers in a pod. When this is set containers will be able to view and signal processes from other containers in the same pod, and the first process in each container will not be assigned PID 1. HostPID and ShareProcessNamespace cannot both be set. Optional: Default to false.")
    subdomain: Optional[StrictStr] = Field(default=None, description="If specified, the fully qualified Pod hostname will be \"<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>\". If not specified, the pod will not have a domainname at all.")
    termination_grace_period_seconds: Optional[StrictInt] = Field(default=None, alias="terminationGracePeriodSeconds", description="Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.")
    tolerations: Optional[conlist(V1Toleration)] = Field(default=None, description="If specified, the pod's tolerations.")
    topology_spread_constraints: Optional[conlist(V1TopologySpreadConstraint)] = Field(default=None, alias="topologySpreadConstraints", description="TopologySpreadConstraints describes how a group of pods ought to spread across topology domains. Scheduler will schedule pods in a way which abides by the constraints. All topologySpreadConstraints are ANDed.")
    volumes: Optional[conlist(V1Volume)] = Field(default=None, description="List of volumes that can be mounted by containers belonging to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes")
    __properties = ["activeDeadlineSeconds", "affinity", "automountServiceAccountToken", "containers", "dnsConfig", "dnsPolicy", "enableServiceLinks", "ephemeralContainers", "hostAliases", "hostIPC", "hostNetwork", "hostPID", "hostUsers", "hostname", "imagePullSecrets", "initContainers", "nodeName", "nodeSelector", "os", "overhead", "preemptionPolicy", "priority", "priorityClassName", "readinessGates", "resourceClaims", "restartPolicy", "runtimeClassName", "schedulerName", "schedulingGates", "securityContext", "serviceAccount", "serviceAccountName", "setHostnameAsFQDN", "shareProcessNamespace", "subdomain", "terminationGracePeriodSeconds", "tolerations", "topologySpreadConstraints", "volumes"]

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
    def from_json(cls, json_str: str) -> V1PodSpec:
        """Create an instance of V1PodSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of affinity
        if self.affinity:
            _dict['affinity'] = self.affinity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in containers (list)
        _items = []
        if self.containers:
            for _item in self.containers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['containers'] = _items
        # override the default output from pydantic by calling `to_dict()` of dns_config
        if self.dns_config:
            _dict['dnsConfig'] = self.dns_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in ephemeral_containers (list)
        _items = []
        if self.ephemeral_containers:
            for _item in self.ephemeral_containers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ephemeralContainers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in host_aliases (list)
        _items = []
        if self.host_aliases:
            for _item in self.host_aliases:
                if _item:
                    _items.append(_item.to_dict())
            _dict['hostAliases'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in image_pull_secrets (list)
        _items = []
        if self.image_pull_secrets:
            for _item in self.image_pull_secrets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['imagePullSecrets'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in init_containers (list)
        _items = []
        if self.init_containers:
            for _item in self.init_containers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['initContainers'] = _items
        # override the default output from pydantic by calling `to_dict()` of os
        if self.os:
            _dict['os'] = self.os.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in readiness_gates (list)
        _items = []
        if self.readiness_gates:
            for _item in self.readiness_gates:
                if _item:
                    _items.append(_item.to_dict())
            _dict['readinessGates'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in resource_claims (list)
        _items = []
        if self.resource_claims:
            for _item in self.resource_claims:
                if _item:
                    _items.append(_item.to_dict())
            _dict['resourceClaims'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in scheduling_gates (list)
        _items = []
        if self.scheduling_gates:
            for _item in self.scheduling_gates:
                if _item:
                    _items.append(_item.to_dict())
            _dict['schedulingGates'] = _items
        # override the default output from pydantic by calling `to_dict()` of security_context
        if self.security_context:
            _dict['securityContext'] = self.security_context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tolerations (list)
        _items = []
        if self.tolerations:
            for _item in self.tolerations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tolerations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in topology_spread_constraints (list)
        _items = []
        if self.topology_spread_constraints:
            for _item in self.topology_spread_constraints:
                if _item:
                    _items.append(_item.to_dict())
            _dict['topologySpreadConstraints'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in volumes (list)
        _items = []
        if self.volumes:
            for _item in self.volumes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['volumes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1PodSpec:
        """Create an instance of V1PodSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1PodSpec.parse_obj(obj)

        _obj = V1PodSpec.parse_obj({
            "active_deadline_seconds": obj.get("activeDeadlineSeconds"),
            "affinity": V1Affinity.from_dict(obj.get("affinity")) if obj.get("affinity") is not None else None,
            "automount_service_account_token": obj.get("automountServiceAccountToken"),
            "containers": [V1Container.from_dict(_item) for _item in obj.get("containers")] if obj.get("containers") is not None else None,
            "dns_config": V1PodDNSConfig.from_dict(obj.get("dnsConfig")) if obj.get("dnsConfig") is not None else None,
            "dns_policy": obj.get("dnsPolicy"),
            "enable_service_links": obj.get("enableServiceLinks"),
            "ephemeral_containers": [V1EphemeralContainer.from_dict(_item) for _item in obj.get("ephemeralContainers")] if obj.get("ephemeralContainers") is not None else None,
            "host_aliases": [V1HostAlias.from_dict(_item) for _item in obj.get("hostAliases")] if obj.get("hostAliases") is not None else None,
            "host_ipc": obj.get("hostIPC"),
            "host_network": obj.get("hostNetwork"),
            "host_pid": obj.get("hostPID"),
            "host_users": obj.get("hostUsers"),
            "hostname": obj.get("hostname"),
            "image_pull_secrets": [V1LocalObjectReference.from_dict(_item) for _item in obj.get("imagePullSecrets")] if obj.get("imagePullSecrets") is not None else None,
            "init_containers": [V1Container.from_dict(_item) for _item in obj.get("initContainers")] if obj.get("initContainers") is not None else None,
            "node_name": obj.get("nodeName"),
            "node_selector": obj.get("nodeSelector"),
            "os": V1PodOS.from_dict(obj.get("os")) if obj.get("os") is not None else None,
            "overhead": obj.get("overhead"),
            "preemption_policy": obj.get("preemptionPolicy"),
            "priority": obj.get("priority"),
            "priority_class_name": obj.get("priorityClassName"),
            "readiness_gates": [V1PodReadinessGate.from_dict(_item) for _item in obj.get("readinessGates")] if obj.get("readinessGates") is not None else None,
            "resource_claims": [V1PodResourceClaim.from_dict(_item) for _item in obj.get("resourceClaims")] if obj.get("resourceClaims") is not None else None,
            "restart_policy": obj.get("restartPolicy"),
            "runtime_class_name": obj.get("runtimeClassName"),
            "scheduler_name": obj.get("schedulerName"),
            "scheduling_gates": [V1PodSchedulingGate.from_dict(_item) for _item in obj.get("schedulingGates")] if obj.get("schedulingGates") is not None else None,
            "security_context": V1PodSecurityContext.from_dict(obj.get("securityContext")) if obj.get("securityContext") is not None else None,
            "service_account": obj.get("serviceAccount"),
            "service_account_name": obj.get("serviceAccountName"),
            "set_hostname_as_fqdn": obj.get("setHostnameAsFQDN"),
            "share_process_namespace": obj.get("shareProcessNamespace"),
            "subdomain": obj.get("subdomain"),
            "termination_grace_period_seconds": obj.get("terminationGracePeriodSeconds"),
            "tolerations": [V1Toleration.from_dict(_item) for _item in obj.get("tolerations")] if obj.get("tolerations") is not None else None,
            "topology_spread_constraints": [V1TopologySpreadConstraint.from_dict(_item) for _item in obj.get("topologySpreadConstraints")] if obj.get("topologySpreadConstraints") is not None else None,
            "volumes": [V1Volume.from_dict(_item) for _item in obj.get("volumes")] if obj.get("volumes") is not None else None
        })
        return _obj


