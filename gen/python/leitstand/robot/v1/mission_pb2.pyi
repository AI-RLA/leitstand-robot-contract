from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StageKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STAGE_KIND_UNSPECIFIED: _ClassVar[StageKind]
    STAGE_KIND_NAVIGATION: _ClassVar[StageKind]

class CancelMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CANCEL_MODE_UNSPECIFIED: _ClassVar[CancelMode]
    CANCEL_MODE_GRACEFUL: _ClassVar[CancelMode]
    CANCEL_MODE_IMMEDIATE: _ClassVar[CancelMode]
STAGE_KIND_UNSPECIFIED: StageKind
STAGE_KIND_NAVIGATION: StageKind
CANCEL_MODE_UNSPECIFIED: CancelMode
CANCEL_MODE_GRACEFUL: CancelMode
CANCEL_MODE_IMMEDIATE: CancelMode

class WGS84Waypoint(_message.Message):
    __slots__ = ("lat", "lon", "heading_deg")
    LAT_FIELD_NUMBER: _ClassVar[int]
    LON_FIELD_NUMBER: _ClassVar[int]
    HEADING_DEG_FIELD_NUMBER: _ClassVar[int]
    lat: float
    lon: float
    heading_deg: float
    def __init__(self, lat: _Optional[float] = ..., lon: _Optional[float] = ..., heading_deg: _Optional[float] = ...) -> None: ...

class SiteLocalWaypoint(_message.Message):
    __slots__ = ("site_id", "x", "y", "theta")
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    THETA_FIELD_NUMBER: _ClassVar[int]
    site_id: str
    x: float
    y: float
    theta: float
    def __init__(self, site_id: _Optional[str] = ..., x: _Optional[float] = ..., y: _Optional[float] = ..., theta: _Optional[float] = ...) -> None: ...

class Waypoint(_message.Message):
    __slots__ = ("wgs84", "site_local")
    WGS84_FIELD_NUMBER: _ClassVar[int]
    SITE_LOCAL_FIELD_NUMBER: _ClassVar[int]
    wgs84: WGS84Waypoint
    site_local: SiteLocalWaypoint
    def __init__(self, wgs84: _Optional[_Union[WGS84Waypoint, _Mapping]] = ..., site_local: _Optional[_Union[SiteLocalWaypoint, _Mapping]] = ...) -> None: ...

class NavigationStage(_message.Message):
    __slots__ = ("waypoints",)
    WAYPOINTS_FIELD_NUMBER: _ClassVar[int]
    waypoints: _containers.RepeatedCompositeFieldContainer[Waypoint]
    def __init__(self, waypoints: _Optional[_Iterable[_Union[Waypoint, _Mapping]]] = ...) -> None: ...

class Stage(_message.Message):
    __slots__ = ("stage_id", "kind", "navigation", "on_cancel")
    STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAVIGATION_FIELD_NUMBER: _ClassVar[int]
    ON_CANCEL_FIELD_NUMBER: _ClassVar[int]
    stage_id: str
    kind: StageKind
    navigation: NavigationStage
    on_cancel: _containers.RepeatedCompositeFieldContainer[Stage]
    def __init__(self, stage_id: _Optional[str] = ..., kind: _Optional[_Union[StageKind, str]] = ..., navigation: _Optional[_Union[NavigationStage, _Mapping]] = ..., on_cancel: _Optional[_Iterable[_Union[Stage, _Mapping]]] = ...) -> None: ...

class Mission(_message.Message):
    __slots__ = ("mission_id", "stages")
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    STAGES_FIELD_NUMBER: _ClassVar[int]
    mission_id: str
    stages: _containers.RepeatedCompositeFieldContainer[Stage]
    def __init__(self, mission_id: _Optional[str] = ..., stages: _Optional[_Iterable[_Union[Stage, _Mapping]]] = ...) -> None: ...

class MissionDispatchRequest(_message.Message):
    __slots__ = ("dispatch_id", "mission")
    DISPATCH_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_FIELD_NUMBER: _ClassVar[int]
    dispatch_id: str
    mission: Mission
    def __init__(self, dispatch_id: _Optional[str] = ..., mission: _Optional[_Union[Mission, _Mapping]] = ...) -> None: ...

class MissionDispatchResponse(_message.Message):
    __slots__ = ("accepted", "reason")
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    accepted: bool
    reason: str
    def __init__(self, accepted: _Optional[bool] = ..., reason: _Optional[str] = ...) -> None: ...

class CancelRequest(_message.Message):
    __slots__ = ("mission_id", "mode")
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    mission_id: str
    mode: CancelMode
    def __init__(self, mission_id: _Optional[str] = ..., mode: _Optional[_Union[CancelMode, str]] = ...) -> None: ...
