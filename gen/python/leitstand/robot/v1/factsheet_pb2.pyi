from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WaypointKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WAYPOINT_KIND_UNSPECIFIED: _ClassVar[WaypointKind]
    WAYPOINT_KIND_WGS84: _ClassVar[WaypointKind]
    WAYPOINT_KIND_SITE_LOCAL: _ClassVar[WaypointKind]
WAYPOINT_KIND_UNSPECIFIED: WaypointKind
WAYPOINT_KIND_WGS84: WaypointKind
WAYPOINT_KIND_SITE_LOCAL: WaypointKind

class NavigationCapability(_message.Message):
    __slots__ = ("supported_waypoint_kinds",)
    SUPPORTED_WAYPOINT_KINDS_FIELD_NUMBER: _ClassVar[int]
    supported_waypoint_kinds: _containers.RepeatedScalarFieldContainer[WaypointKind]
    def __init__(self, supported_waypoint_kinds: _Optional[_Iterable[_Union[WaypointKind, str]]] = ...) -> None: ...

class CoverageCapability(_message.Message):
    __slots__ = ("supported_waypoint_kinds",)
    SUPPORTED_WAYPOINT_KINDS_FIELD_NUMBER: _ClassVar[int]
    supported_waypoint_kinds: _containers.RepeatedScalarFieldContainer[WaypointKind]
    def __init__(self, supported_waypoint_kinds: _Optional[_Iterable[_Union[WaypointKind, str]]] = ...) -> None: ...

class StageCapability(_message.Message):
    __slots__ = ("navigation", "coverage")
    NAVIGATION_FIELD_NUMBER: _ClassVar[int]
    COVERAGE_FIELD_NUMBER: _ClassVar[int]
    navigation: NavigationCapability
    coverage: CoverageCapability
    def __init__(self, navigation: _Optional[_Union[NavigationCapability, _Mapping]] = ..., coverage: _Optional[_Union[CoverageCapability, _Mapping]] = ...) -> None: ...

class PhysicalParameters(_message.Message):
    __slots__ = ("track_width_m", "min_turning_radius_m")
    TRACK_WIDTH_M_FIELD_NUMBER: _ClassVar[int]
    MIN_TURNING_RADIUS_M_FIELD_NUMBER: _ClassVar[int]
    track_width_m: float
    min_turning_radius_m: float
    def __init__(self, track_width_m: _Optional[float] = ..., min_turning_radius_m: _Optional[float] = ...) -> None: ...

class Factsheet(_message.Message):
    __slots__ = ("stage_capabilities", "physical_parameters")
    STAGE_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    stage_capabilities: _containers.RepeatedCompositeFieldContainer[StageCapability]
    physical_parameters: PhysicalParameters
    def __init__(self, stage_capabilities: _Optional[_Iterable[_Union[StageCapability, _Mapping]]] = ..., physical_parameters: _Optional[_Union[PhysicalParameters, _Mapping]] = ...) -> None: ...
