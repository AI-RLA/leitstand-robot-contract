from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlRefusal(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTROL_REFUSAL_UNSPECIFIED: _ClassVar[ControlRefusal]
    CONTROL_REFUSAL_NOT_EXECUTING_RUN: _ClassVar[ControlRefusal]
    CONTROL_REFUSAL_OTHER: _ClassVar[ControlRefusal]
CONTROL_REFUSAL_UNSPECIFIED: ControlRefusal
CONTROL_REFUSAL_NOT_EXECUTING_RUN: ControlRefusal
CONTROL_REFUSAL_OTHER: ControlRefusal

class ControlRequest(_message.Message):
    __slots__ = ("run_id",)
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class ControlResponse(_message.Message):
    __slots__ = ("applied", "reason", "refusal")
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    applied: bool
    reason: str
    refusal: ControlRefusal
    def __init__(self, applied: _Optional[bool] = ..., reason: _Optional[str] = ..., refusal: _Optional[_Union[ControlRefusal, str]] = ...) -> None: ...
