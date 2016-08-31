# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: behavior.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='behavior.proto',
  package='behavior',
  syntax='proto2',
  serialized_pb=_b('\n\x0e\x62\x65havior.proto\x12\x08\x62\x65havior\"\x97\x02\n\x04\x44\x61ta\x12$\n\x08position\x18\x01 \x02(\x0b\x32\x12.behavior.Position\x12$\n\x08velocity\x18\x02 \x02(\x0b\x32\x12.behavior.Position\x12\x10\n\x08response\x18\x03 \x02(\x08\x12\x0e\n\x06reward\x18\x04 \x02(\x08\x12\x13\n\x0btrialNumber\x18\x05 \x02(\r\x12$\n\x0cwallDistance\x18\x06 \x02(\x0b\x32\x0e.behavior.Wall\x12\x0c\n\x04link\x18\x07 \x02(\x08\x12\x11\n\tcollision\x18\x08 \x02(\x08\x12\x0f\n\x07\x61\x64vance\x18\t \x02(\x08\x12\x11\n\tdeltaTime\x18\n \x02(\r\x12\x13\n\x0b\x65lapsedTime\x18\x0b \x02(\r\x12\x0c\n\x04time\x18\x0c \x02(\r\",\n\x08Position\x12\x0f\n\x07\x66orward\x18\x01 \x02(\x02\x12\x0f\n\x07lateral\x18\x02 \x02(\x02\"4\n\x04Wall\x12\r\n\x05right\x18\x01 \x02(\x02\x12\x0f\n\x07\x66orward\x18\x02 \x02(\x02\x12\x0c\n\x04left\x18\x03 \x02(\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='behavior.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='behavior.Data.position', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='behavior.Data.velocity', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='response', full_name='behavior.Data.response', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reward', full_name='behavior.Data.reward', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trialNumber', full_name='behavior.Data.trialNumber', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wallDistance', full_name='behavior.Data.wallDistance', index=5,
      number=6, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='link', full_name='behavior.Data.link', index=6,
      number=7, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='collision', full_name='behavior.Data.collision', index=7,
      number=8, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='advance', full_name='behavior.Data.advance', index=8,
      number=9, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deltaTime', full_name='behavior.Data.deltaTime', index=9,
      number=10, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='elapsedTime', full_name='behavior.Data.elapsedTime', index=10,
      number=11, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='behavior.Data.time', index=11,
      number=12, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=308,
)


_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='behavior.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='forward', full_name='behavior.Position.forward', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lateral', full_name='behavior.Position.lateral', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=310,
  serialized_end=354,
)


_WALL = _descriptor.Descriptor(
  name='Wall',
  full_name='behavior.Wall',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='right', full_name='behavior.Wall.right', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forward', full_name='behavior.Wall.forward', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='left', full_name='behavior.Wall.left', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=356,
  serialized_end=408,
)

_DATA.fields_by_name['position'].message_type = _POSITION
_DATA.fields_by_name['velocity'].message_type = _POSITION
_DATA.fields_by_name['wallDistance'].message_type = _WALL
DESCRIPTOR.message_types_by_name['Data'] = _DATA
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
DESCRIPTOR.message_types_by_name['Wall'] = _WALL

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), dict(
  DESCRIPTOR = _DATA,
  __module__ = 'behavior_pb2'
  # @@protoc_insertion_point(class_scope:behavior.Data)
  ))
_sym_db.RegisterMessage(Data)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), dict(
  DESCRIPTOR = _POSITION,
  __module__ = 'behavior_pb2'
  # @@protoc_insertion_point(class_scope:behavior.Position)
  ))
_sym_db.RegisterMessage(Position)

Wall = _reflection.GeneratedProtocolMessageType('Wall', (_message.Message,), dict(
  DESCRIPTOR = _WALL,
  __module__ = 'behavior_pb2'
  # @@protoc_insertion_point(class_scope:behavior.Wall)
  ))
_sym_db.RegisterMessage(Wall)


# @@protoc_insertion_point(module_scope)
