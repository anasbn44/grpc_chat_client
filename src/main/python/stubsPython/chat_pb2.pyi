from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

ALREADY_EXIST: ResponseType
DESCRIPTOR: _descriptor.FileDescriptor
DISCONNECTED: ResponseType
FAILED: ResponseType
ISCONNECTED: ResponseType
JOINED: ResponseType
LEFT: ResponseType
RECIEVED: ResponseType
SENT: ResponseType

class Channel(_message.Message):
    __slots__ = ["chanelName", "client"]
    CHANELNAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    chanelName: str
    client: Client
    def __init__(self, chanelName: _Optional[str] = ..., client: _Optional[_Union[Client, _Mapping]] = ...) -> None: ...

class Client(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ["channel", "text"]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    channel: Channel
    text: str
    def __init__(self, channel: _Optional[_Union[Channel, _Mapping]] = ..., text: _Optional[str] = ..., **kwargs) -> None: ...

class Response(_message.Message):
    __slots__ = ["message", "timestamp", "type"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    message: str
    timestamp: _timestamp_pb2.Timestamp
    type: ResponseType
    def __init__(self, type: _Optional[_Union[ResponseType, str]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class ResponseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
