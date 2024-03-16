# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openscenario_msgs/environment.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from openscenario_msgs import boundingbox_pb2 as openscenario__msgs_dot_boundingbox__pb2
from openscenario_msgs import file_pb2 as openscenario__msgs_dot_file__pb2
from openscenario_msgs import parameter_pb2 as openscenario__msgs_dot_parameter__pb2
from openscenario_msgs import property_pb2 as openscenario__msgs_dot_property__pb2
from openscenario_msgs import time_of_day_pb2 as openscenario__msgs_dot_time__of__day__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#openscenario_msgs/environment.proto\x12\x0copenscenario\x1a#openscenario_msgs/boundingbox.proto\x1a\x1copenscenario_msgs/file.proto\x1a!openscenario_msgs/parameter.proto\x1a openscenario_msgs/property.proto\x1a#openscenario_msgs/time_of_day.proto\"\xe6\x01\n\x0b\x45nvironment\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x41\n\x15parameterDeclarations\x18\x02 \x03(\x0b\x32\".openscenario.ParameterDeclaration\x12*\n\ttimeOfDay\x18\x03 \x01(\x0b\x32\x17.openscenario.TimeOfDay\x12&\n\x07weather\x18\x04 \x01(\x0b\x32\x15.openscenario.Weather\x12\x32\n\rroadCondition\x18\x05 \x01(\x0b\x32\x1b.openscenario.RoadCondition\"\xbf\x02\n\x07Weather\x12\x1b\n\x13\x61tmosphericPressure\x18\x01 \x01(\x01\x12@\n\x14\x66ractionalCloudCover\x18\x02 \x01(\x0e\x32\".openscenario.FractionalCloudCover\x12\x13\n\x0btemperature\x18\x03 \x01(\x01\x12\x1e\n\x03sun\x18\x04 \x01(\x0b\x32\x11.openscenario.Sun\x12\x1e\n\x03\x66og\x18\x05 \x01(\x0b\x32\x11.openscenario.Fog\x12\x32\n\rprecipitation\x18\x06 \x01(\x0b\x32\x1b.openscenario.Precipitation\x12 \n\x04wind\x18\x07 \x01(\x0b\x32\x12.openscenario.Wind\x12*\n\tdomeImage\x18\x08 \x01(\x0b\x32\x17.openscenario.DomeImage\"J\n\x03\x46og\x12\x13\n\x0bvisualRange\x18\x01 \x02(\x01\x12.\n\x0b\x62oundingBox\x18\x02 \x01(\x0b\x32\x19.openscenario.BoundingBox\"k\n\rPrecipitation\x12\x1e\n\x16precipitationIntensity\x18\x01 \x01(\x01\x12:\n\x11precipitationType\x18\x02 \x02(\x0e\x32\x1f.openscenario.PrecipitationType\">\n\x03Sun\x12\x0f\n\x07\x61zimuth\x18\x01 \x02(\x01\x12\x11\n\televation\x18\x02 \x02(\x01\x12\x13\n\x0billuminance\x18\x03 \x01(\x01\"(\n\x04Wind\x12\x11\n\tdirection\x18\x01 \x02(\x01\x12\r\n\x05speed\x18\x02 \x02(\x01\"H\n\tDomeImage\x12\x15\n\razimuthOffset\x18\x01 \x01(\x01\x12$\n\x08\x64omeFile\x18\x02 \x02(\x0b\x32\x12.openscenario.File\"\x82\x01\n\rRoadCondition\x12\x1b\n\x13\x66rictionScaleFactor\x18\x01 \x02(\x01\x12&\n\x07wetness\x18\x02 \x01(\x0e\x32\x15.openscenario.Wetness\x12,\n\nproperties\x18\x03 \x01(\x0b\x32\x18.openscenario.Properties*\x88\x03\n\x14\x46ractionalCloudCover\x12#\n\x1f\x46RACTIONALCLOUDCOVER_ZERO_OKTAS\x10\x00\x12\"\n\x1e\x46RACTIONALCLOUDCOVER_ONE_OKTAS\x10\x01\x12\"\n\x1e\x46RACTIONALCLOUDCOVER_TWO_OKTAS\x10\x02\x12$\n FRACTIONALCLOUDCOVER_THREE_OKTAS\x10\x03\x12#\n\x1f\x46RACTIONALCLOUDCOVER_FOUR_OKTAS\x10\x04\x12#\n\x1f\x46RACTIONALCLOUDCOVER_FIVE_OKTAS\x10\x05\x12\"\n\x1e\x46RACTIONALCLOUDCOVER_SIX_OKTAS\x10\x06\x12$\n FRACTIONALCLOUDCOVER_SEVEN_OKTAS\x10\x07\x12$\n FRACTIONALCLOUDCOVER_EIGHT_OKTAS\x10\x08\x12#\n\x1f\x46RACTIONALCLOUDCOVER_NINE_OKTAS\x10\t*f\n\x11PrecipitationType\x12\x19\n\x15PRECIPITATIONTYPE_DRY\x10\x00\x12\x1a\n\x16PRECIPITATIONTYPE_RAIN\x10\x01\x12\x1a\n\x16PRECIPITATIONTYPE_SNOW\x10\x02*~\n\x07Wetness\x12\x0f\n\x0bWETNESS_DRY\x10\x00\x12\x11\n\rWETNESS_MOIST\x10\x01\x12\x1c\n\x18WETNESS_WET_WITH_PUDDLES\x10\x02\x12\x17\n\x13WETNESS_LOW_FLOODED\x10\x03\x12\x18\n\x14WETNESS_HIGH_FLOODED\x10\x04')

_FRACTIONALCLOUDCOVER = DESCRIPTOR.enum_types_by_name['FractionalCloudCover']
FractionalCloudCover = enum_type_wrapper.EnumTypeWrapper(_FRACTIONALCLOUDCOVER)
_PRECIPITATIONTYPE = DESCRIPTOR.enum_types_by_name['PrecipitationType']
PrecipitationType = enum_type_wrapper.EnumTypeWrapper(_PRECIPITATIONTYPE)
_WETNESS = DESCRIPTOR.enum_types_by_name['Wetness']
Wetness = enum_type_wrapper.EnumTypeWrapper(_WETNESS)
FRACTIONALCLOUDCOVER_ZERO_OKTAS = 0
FRACTIONALCLOUDCOVER_ONE_OKTAS = 1
FRACTIONALCLOUDCOVER_TWO_OKTAS = 2
FRACTIONALCLOUDCOVER_THREE_OKTAS = 3
FRACTIONALCLOUDCOVER_FOUR_OKTAS = 4
FRACTIONALCLOUDCOVER_FIVE_OKTAS = 5
FRACTIONALCLOUDCOVER_SIX_OKTAS = 6
FRACTIONALCLOUDCOVER_SEVEN_OKTAS = 7
FRACTIONALCLOUDCOVER_EIGHT_OKTAS = 8
FRACTIONALCLOUDCOVER_NINE_OKTAS = 9
PRECIPITATIONTYPE_DRY = 0
PRECIPITATIONTYPE_RAIN = 1
PRECIPITATIONTYPE_SNOW = 2
WETNESS_DRY = 0
WETNESS_MOIST = 1
WETNESS_WET_WITH_PUDDLES = 2
WETNESS_LOW_FLOODED = 3
WETNESS_HIGH_FLOODED = 4


_ENVIRONMENT = DESCRIPTOR.message_types_by_name['Environment']
_WEATHER = DESCRIPTOR.message_types_by_name['Weather']
_FOG = DESCRIPTOR.message_types_by_name['Fog']
_PRECIPITATION = DESCRIPTOR.message_types_by_name['Precipitation']
_SUN = DESCRIPTOR.message_types_by_name['Sun']
_WIND = DESCRIPTOR.message_types_by_name['Wind']
_DOMEIMAGE = DESCRIPTOR.message_types_by_name['DomeImage']
_ROADCONDITION = DESCRIPTOR.message_types_by_name['RoadCondition']
Environment = _reflection.GeneratedProtocolMessageType('Environment', (_message.Message,), {
  'DESCRIPTOR' : _ENVIRONMENT,
  '__module__' : 'openscenario_msgs.environment_pb2'
  # @@protoc_insertion_point(class_scope:openscenario.Environment)
  })
_sym_db.RegisterMessage(Environment)

Weather = _reflection.GeneratedProtocolMessageType('Weather', (_message.Message,), {
  'DESCRIPTOR' : _WEATHER,
  '__module__' : 'openscenario_msgs.environment_pb2'
  # @@protoc_insertion_point(class_scope:openscenario.Weather)
  })
_sym_db.RegisterMessage(Weather)

Fog = _reflection.GeneratedProtocolMessageType('Fog', (_message.Message,), {
  'DESCRIPTOR' : _FOG,
  '__module__' : 'openscenario_msgs.environment_pb2'
  # @@protoc_insertion_point(class_scope:openscenario.Fog)
  })
_sym_db.RegisterMessage(Fog)

Precipitation = _reflection.GeneratedProtocolMessageType('Precipitation', (_message.Message,), {
  'DESCRIPTOR' : _PRECIPITATION,
  '__module__' : 'openscenario_msgs.environment_pb2'
  # @@protoc_insertion_point(class_scope:openscenario.Precipitation)
  })
_sym_db.RegisterMessage(Precipitation)

Sun = _reflection.GeneratedProtocolMessageType('Sun', (_message.Message,), {
  'DESCRIPTOR' : _SUN,
  '__module__' : 'openscenario_msgs.environment_pb2'
  # @@protoc_insertion_point(class_scope:openscenario.Sun)
  })
_sym_db.RegisterMessage(Sun)

Wind = _reflection.GeneratedProtocolMessageType('Wind', (_message.Message,), {
  'DESCRIPTOR' : _WIND,
  '__module__' : 'openscenario_msgs.environment_pb2'
  # @@protoc_insertion_point(class_scope:openscenario.Wind)
  })
_sym_db.RegisterMessage(Wind)

DomeImage = _reflection.GeneratedProtocolMessageType('DomeImage', (_message.Message,), {
  'DESCRIPTOR' : _DOMEIMAGE,
  '__module__' : 'openscenario_msgs.environment_pb2'
  # @@protoc_insertion_point(class_scope:openscenario.DomeImage)
  })
_sym_db.RegisterMessage(DomeImage)

RoadCondition = _reflection.GeneratedProtocolMessageType('RoadCondition', (_message.Message,), {
  'DESCRIPTOR' : _ROADCONDITION,
  '__module__' : 'openscenario_msgs.environment_pb2'
  # @@protoc_insertion_point(class_scope:openscenario.RoadCondition)
  })
_sym_db.RegisterMessage(RoadCondition)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FRACTIONALCLOUDCOVER._serialized_start=1280
  _FRACTIONALCLOUDCOVER._serialized_end=1672
  _PRECIPITATIONTYPE._serialized_start=1674
  _PRECIPITATIONTYPE._serialized_end=1776
  _WETNESS._serialized_start=1778
  _WETNESS._serialized_end=1904
  _ENVIRONMENT._serialized_start=227
  _ENVIRONMENT._serialized_end=457
  _WEATHER._serialized_start=460
  _WEATHER._serialized_end=779
  _FOG._serialized_start=781
  _FOG._serialized_end=855
  _PRECIPITATION._serialized_start=857
  _PRECIPITATION._serialized_end=964
  _SUN._serialized_start=966
  _SUN._serialized_end=1028
  _WIND._serialized_start=1030
  _WIND._serialized_end=1070
  _DOMEIMAGE._serialized_start=1072
  _DOMEIMAGE._serialized_end=1144
  _ROADCONDITION._serialized_start=1147
  _ROADCONDITION._serialized_end=1277
# @@protoc_insertion_point(module_scope)
