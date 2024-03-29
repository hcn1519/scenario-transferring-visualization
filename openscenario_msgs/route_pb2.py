# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openscenario_msgs/route.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from openscenario_msgs import parameter_pb2 as openscenario__msgs_dot_parameter__pb2
from openscenario_msgs import position_pb2 as openscenario__msgs_dot_position__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dopenscenario_msgs/route.proto\x12\x0copenscenario\x1a!openscenario_msgs/parameter.proto\x1a openscenario_msgs/position.proto\"\x93\x01\n\x05Route\x12\x0e\n\x06\x63losed\x18\x01 \x02(\x08\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x41\n\x15parameterDeclarations\x18\x03 \x03(\x0b\x32\".openscenario.ParameterDeclaration\x12)\n\twaypoints\x18\x04 \x03(\x0b\x32\x16.openscenario.Waypoint\"h\n\x08Waypoint\x12\x32\n\rrouteStrategy\x18\x01 \x02(\x0e\x32\x1b.openscenario.RouteStrategy\x12(\n\x08position\x18\x02 \x02(\x0b\x32\x16.openscenario.Position*\x87\x01\n\rRouteStrategy\x12\x19\n\x15ROUTESTRATEGY_FASTEST\x10\x00\x12%\n!ROUTESTRATEGY_LEAST_INTERSECTIONS\x10\x01\x12\x18\n\x14ROUTESTRATEGY_RANDOM\x10\x02\x12\x1a\n\x16ROUTESTRATEGY_SHORTEST\x10\x03')

_ROUTESTRATEGY = DESCRIPTOR.enum_types_by_name['RouteStrategy']
RouteStrategy = enum_type_wrapper.EnumTypeWrapper(_ROUTESTRATEGY)
ROUTESTRATEGY_FASTEST = 0
ROUTESTRATEGY_LEAST_INTERSECTIONS = 1
ROUTESTRATEGY_RANDOM = 2
ROUTESTRATEGY_SHORTEST = 3


_ROUTE = DESCRIPTOR.message_types_by_name['Route']
_WAYPOINT = DESCRIPTOR.message_types_by_name['Waypoint']
Route = _reflection.GeneratedProtocolMessageType('Route', (_message.Message,), {
  'DESCRIPTOR' : _ROUTE,
  '__module__' : 'openscenario_msgs.route_pb2'
  # @@protoc_insertion_point(class_scope:openscenario.Route)
  })
_sym_db.RegisterMessage(Route)

Waypoint = _reflection.GeneratedProtocolMessageType('Waypoint', (_message.Message,), {
  'DESCRIPTOR' : _WAYPOINT,
  '__module__' : 'openscenario_msgs.route_pb2'
  # @@protoc_insertion_point(class_scope:openscenario.Waypoint)
  })
_sym_db.RegisterMessage(Waypoint)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ROUTESTRATEGY._serialized_start=373
  _ROUTESTRATEGY._serialized_end=508
  _ROUTE._serialized_start=117
  _ROUTE._serialized_end=264
  _WAYPOINT._serialized_start=266
  _WAYPOINT._serialized_end=370
# @@protoc_insertion_point(module_scope)
