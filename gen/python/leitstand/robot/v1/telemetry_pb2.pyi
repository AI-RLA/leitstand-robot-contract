import datetime

from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Pose(_message.Message):
    __slots__ = ("timestamp", "lat", "lon", "heading_deg", "horizontal_accuracy_m")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LAT_FIELD_NUMBER: _ClassVar[int]
    LON_FIELD_NUMBER: _ClassVar[int]
    HEADING_DEG_FIELD_NUMBER: _ClassVar[int]
    HORIZONTAL_ACCURACY_M_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    lat: float
    lon: float
    heading_deg: float
    horizontal_accuracy_m: float
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., lat: _Optional[float] = ..., lon: _Optional[float] = ..., heading_deg: _Optional[float] = ..., horizontal_accuracy_m: _Optional[float] = ...) -> None: ...

class Battery(_message.Message):
    __slots__ = ("timestamp", "battery_pct", "charging")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    BATTERY_PCT_FIELD_NUMBER: _ClassVar[int]
    CHARGING_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    battery_pct: int
    charging: bool
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., battery_pct: _Optional[int] = ..., charging: _Optional[bool] = ...) -> None: ...
