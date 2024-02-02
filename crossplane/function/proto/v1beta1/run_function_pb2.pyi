from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Ready(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    READY_UNSPECIFIED: _ClassVar[Ready]
    READY_TRUE: _ClassVar[Ready]
    READY_FALSE: _ClassVar[Ready]

class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEVERITY_UNSPECIFIED: _ClassVar[Severity]
    SEVERITY_FATAL: _ClassVar[Severity]
    SEVERITY_WARNING: _ClassVar[Severity]
    SEVERITY_NORMAL: _ClassVar[Severity]
READY_UNSPECIFIED: Ready
READY_TRUE: Ready
READY_FALSE: Ready
SEVERITY_UNSPECIFIED: Severity
SEVERITY_FATAL: Severity
SEVERITY_WARNING: Severity
SEVERITY_NORMAL: Severity

class RunFunctionRequest(_message.Message):
    __slots__ = ("meta", "observed", "desired", "input", "context", "extra_resources")
    class ExtraResourcesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Resources
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Resources, _Mapping]] = ...) -> None: ...
    META_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_FIELD_NUMBER: _ClassVar[int]
    DESIRED_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EXTRA_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    meta: RequestMeta
    observed: State
    desired: State
    input: _struct_pb2.Struct
    context: _struct_pb2.Struct
    extra_resources: _containers.MessageMap[str, Resources]
    def __init__(self, meta: _Optional[_Union[RequestMeta, _Mapping]] = ..., observed: _Optional[_Union[State, _Mapping]] = ..., desired: _Optional[_Union[State, _Mapping]] = ..., input: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., context: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., extra_resources: _Optional[_Mapping[str, Resources]] = ...) -> None: ...

class Resources(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Resource]
    def __init__(self, items: _Optional[_Iterable[_Union[Resource, _Mapping]]] = ...) -> None: ...

class RunFunctionResponse(_message.Message):
    __slots__ = ("meta", "desired", "results", "context", "requirements")
    META_FIELD_NUMBER: _ClassVar[int]
    DESIRED_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    meta: ResponseMeta
    desired: State
    results: _containers.RepeatedCompositeFieldContainer[Result]
    context: _struct_pb2.Struct
    requirements: Requirements
    def __init__(self, meta: _Optional[_Union[ResponseMeta, _Mapping]] = ..., desired: _Optional[_Union[State, _Mapping]] = ..., results: _Optional[_Iterable[_Union[Result, _Mapping]]] = ..., context: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., requirements: _Optional[_Union[Requirements, _Mapping]] = ...) -> None: ...

class RequestMeta(_message.Message):
    __slots__ = ("tag",)
    TAG_FIELD_NUMBER: _ClassVar[int]
    tag: str
    def __init__(self, tag: _Optional[str] = ...) -> None: ...

class Requirements(_message.Message):
    __slots__ = ("extra_resources",)
    class ExtraResourcesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ResourceSelector
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ResourceSelector, _Mapping]] = ...) -> None: ...
    EXTRA_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    extra_resources: _containers.MessageMap[str, ResourceSelector]
    def __init__(self, extra_resources: _Optional[_Mapping[str, ResourceSelector]] = ...) -> None: ...

class ResourceSelector(_message.Message):
    __slots__ = ("api_version", "kind", "match_name", "match_labels")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    MATCH_NAME_FIELD_NUMBER: _ClassVar[int]
    MATCH_LABELS_FIELD_NUMBER: _ClassVar[int]
    api_version: str
    kind: str
    match_name: str
    match_labels: MatchLabels
    def __init__(self, api_version: _Optional[str] = ..., kind: _Optional[str] = ..., match_name: _Optional[str] = ..., match_labels: _Optional[_Union[MatchLabels, _Mapping]] = ...) -> None: ...

class MatchLabels(_message.Message):
    __slots__ = ("labels",)
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LABELS_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.ScalarMap[str, str]
    def __init__(self, labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ResponseMeta(_message.Message):
    __slots__ = ("tag", "ttl")
    TAG_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    tag: str
    ttl: _duration_pb2.Duration
    def __init__(self, tag: _Optional[str] = ..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class State(_message.Message):
    __slots__ = ("composite", "resources")
    class ResourcesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Resource
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Resource, _Mapping]] = ...) -> None: ...
    COMPOSITE_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    composite: Resource
    resources: _containers.MessageMap[str, Resource]
    def __init__(self, composite: _Optional[_Union[Resource, _Mapping]] = ..., resources: _Optional[_Mapping[str, Resource]] = ...) -> None: ...

class Resource(_message.Message):
    __slots__ = ("resource", "connection_details", "ready")
    class ConnectionDetailsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    READY_FIELD_NUMBER: _ClassVar[int]
    resource: _struct_pb2.Struct
    connection_details: _containers.ScalarMap[str, bytes]
    ready: Ready
    def __init__(self, resource: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., connection_details: _Optional[_Mapping[str, bytes]] = ..., ready: _Optional[_Union[Ready, str]] = ...) -> None: ...

class Result(_message.Message):
    __slots__ = ("severity", "message")
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    severity: Severity
    message: str
    def __init__(self, severity: _Optional[_Union[Severity, str]] = ..., message: _Optional[str] = ...) -> None: ...
