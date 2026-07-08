import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StageStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STAGE_STATUS_UNSPECIFIED: _ClassVar[StageStatus]
    STAGE_STATUS_WAITING: _ClassVar[StageStatus]
    STAGE_STATUS_INITIALIZING: _ClassVar[StageStatus]
    STAGE_STATUS_RUNNING: _ClassVar[StageStatus]
    STAGE_STATUS_PAUSED: _ClassVar[StageStatus]
    STAGE_STATUS_FINISHED: _ClassVar[StageStatus]
    STAGE_STATUS_FAILED: _ClassVar[StageStatus]

class MissionExecStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MISSION_EXEC_STATUS_UNSPECIFIED: _ClassVar[MissionExecStatus]
    MISSION_EXEC_STATUS_RUNNING: _ClassVar[MissionExecStatus]
    MISSION_EXEC_STATUS_PAUSED: _ClassVar[MissionExecStatus]
    MISSION_EXEC_STATUS_SUCCEEDED: _ClassVar[MissionExecStatus]
    MISSION_EXEC_STATUS_FAILED: _ClassVar[MissionExecStatus]
    MISSION_EXEC_STATUS_CANCELLED: _ClassVar[MissionExecStatus]

class ErrorSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ERROR_SEVERITY_UNSPECIFIED: _ClassVar[ErrorSeverity]
    ERROR_SEVERITY_WARNING: _ClassVar[ErrorSeverity]
    ERROR_SEVERITY_FATAL: _ClassVar[ErrorSeverity]
STAGE_STATUS_UNSPECIFIED: StageStatus
STAGE_STATUS_WAITING: StageStatus
STAGE_STATUS_INITIALIZING: StageStatus
STAGE_STATUS_RUNNING: StageStatus
STAGE_STATUS_PAUSED: StageStatus
STAGE_STATUS_FINISHED: StageStatus
STAGE_STATUS_FAILED: StageStatus
MISSION_EXEC_STATUS_UNSPECIFIED: MissionExecStatus
MISSION_EXEC_STATUS_RUNNING: MissionExecStatus
MISSION_EXEC_STATUS_PAUSED: MissionExecStatus
MISSION_EXEC_STATUS_SUCCEEDED: MissionExecStatus
MISSION_EXEC_STATUS_FAILED: MissionExecStatus
MISSION_EXEC_STATUS_CANCELLED: MissionExecStatus
ERROR_SEVERITY_UNSPECIFIED: ErrorSeverity
ERROR_SEVERITY_WARNING: ErrorSeverity
ERROR_SEVERITY_FATAL: ErrorSeverity

class ErrorReference(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ("severity", "type", "references", "description")
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REFERENCES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    severity: ErrorSeverity
    type: str
    references: _containers.RepeatedCompositeFieldContainer[ErrorReference]
    description: str
    def __init__(self, severity: _Optional[_Union[ErrorSeverity, str]] = ..., type: _Optional[str] = ..., references: _Optional[_Iterable[_Union[ErrorReference, _Mapping]]] = ..., description: _Optional[str] = ...) -> None: ...

class StageState(_message.Message):
    __slots__ = ("stage_id", "status", "started_at", "ended_at", "progress", "result")
    class ResultEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    stage_id: str
    status: StageStatus
    started_at: _timestamp_pb2.Timestamp
    ended_at: _timestamp_pb2.Timestamp
    progress: float
    result: _containers.ScalarMap[str, str]
    def __init__(self, stage_id: _Optional[str] = ..., status: _Optional[_Union[StageStatus, str]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ended_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., progress: _Optional[float] = ..., result: _Optional[_Mapping[str, str]] = ...) -> None: ...

class MissionState(_message.Message):
    __slots__ = ("mission_id", "header_id", "timestamp", "exec_status", "current_stage_index", "stage_states", "errors")
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    HEADER_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EXEC_STATUS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STAGE_INDEX_FIELD_NUMBER: _ClassVar[int]
    STAGE_STATES_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    mission_id: str
    header_id: int
    timestamp: _timestamp_pb2.Timestamp
    exec_status: MissionExecStatus
    current_stage_index: int
    stage_states: _containers.RepeatedCompositeFieldContainer[StageState]
    errors: _containers.RepeatedCompositeFieldContainer[Error]
    def __init__(self, mission_id: _Optional[str] = ..., header_id: _Optional[int] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., exec_status: _Optional[_Union[MissionExecStatus, str]] = ..., current_stage_index: _Optional[int] = ..., stage_states: _Optional[_Iterable[_Union[StageState, _Mapping]]] = ..., errors: _Optional[_Iterable[_Union[Error, _Mapping]]] = ...) -> None: ...
