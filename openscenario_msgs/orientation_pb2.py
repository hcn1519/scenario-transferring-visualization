# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openscenario_msgs/orientation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#openscenario_msgs/orientation.proto\x12\x0copenscenario\"\\\n\x0bOrientation\x12\t\n\x01h\x18\x01 \x01(\x01\x12\t\n\x01p\x18\x02 \x01(\x01\x12\t\n\x01r\x18\x03 \x01(\x01\x12,\n\x04type\x18\x04 \x01(\x0e\x32\x1e.openscenario.ReferenceContext*P\n\x10ReferenceContext\x12\x1d\n\x19REFERENCECONTEXT_ABSOLUTE\x10\x00\x12\x1d\n\x19REFERENCECONTEXT_RELATIVE\x10\x01')

_REFERENCECONTEXT = DESCRIPTOR.enum_types_by_name['ReferenceContext']
ReferenceContext = enum_type_wrapper.EnumTypeWrapper(_REFERENCECONTEXT)
REFERENCECONTEXT_ABSOLUTE = 0
REFERENCECONTEXT_RELATIVE = 1


_ORIENTATION = DESCRIPTOR.message_types_by_name['Orientation']
Orientation = _reflection.GeneratedProtocolMessageType('Orientation', (_message.Message,), {
  'DESCRIPTOR' : _ORIENTATION,
  '__module__' : 'openscenario_msgs.orientation_pb2'
  # @@protoc_insertion_point(class_scope:openscenario.Orientation)
  })
_sym_db.RegisterMessage(Orientation)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REFERENCECONTEXT._serialized_start=147
  _REFERENCECONTEXT._serialized_end=227
  _ORIENTATION._serialized_start=53
  _ORIENTATION._serialized_end=145
# @@protoc_insertion_point(module_scope)