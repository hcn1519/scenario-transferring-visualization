# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/drivers/proto/sensor_image.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/drivers/proto/sensor_image.proto',
  package='apollo.drivers',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n(modules/drivers/proto/sensor_image.proto\x12\x0e\x61pollo.drivers\x1a!modules/common/proto/header.proto\"\xa7\x01\n\x05Image\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x10\n\x08\x66rame_id\x18\x02 \x01(\t\x12\x18\n\x10measurement_time\x18\x03 \x01(\x01\x12\x0e\n\x06height\x18\x04 \x01(\r\x12\r\n\x05width\x18\x05 \x01(\r\x12\x10\n\x08\x65ncoding\x18\x06 \x01(\t\x12\x0c\n\x04step\x18\x07 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x08 \x01(\x0c\"\x96\x01\n\x0f\x43ompressedImage\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x10\n\x08\x66rame_id\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\x12\x18\n\x10measurement_time\x18\x05 \x01(\x01\x12\x12\n\nframe_type\x18\x06 \x01(\r*\xfb\x05\n\x0bPixelFormat\x12\t\n\x04RGB8\x10\xe9\x07\x12\n\n\x05RGBA8\x10\xea\x07\x12\n\n\x05RGB16\x10\xeb\x07\x12\x0b\n\x06RGBA16\x10\xec\x07\x12\t\n\x04\x42GR8\x10\xed\x07\x12\n\n\x05\x42GRA8\x10\xee\x07\x12\n\n\x05\x42GR16\x10\xef\x07\x12\x0b\n\x06\x42GRA16\x10\xf0\x07\x12\n\n\x05MONO8\x10\xf1\x07\x12\x0b\n\x06MONO16\x10\xf2\x07\x12\x0e\n\tTYPE_8UC1\x10\xd1\x0f\x12\x0e\n\tTYPE_8UC2\x10\xd2\x0f\x12\x0e\n\tTYPE_8UC3\x10\xd3\x0f\x12\x0e\n\tTYPE_8UC4\x10\xd4\x0f\x12\x0e\n\tTYPE_8SC1\x10\xd5\x0f\x12\x0e\n\tTYPE_8SC2\x10\xd6\x0f\x12\x0e\n\tTYPE_8SC3\x10\xd7\x0f\x12\x0e\n\tTYPE_8SC4\x10\xd8\x0f\x12\x0f\n\nTYPE_16UC1\x10\xd9\x0f\x12\x0f\n\nTYPE_16UC2\x10\xda\x0f\x12\x0f\n\nTYPE_16UC3\x10\xdb\x0f\x12\x0f\n\nTYPE_16UC4\x10\xdc\x0f\x12\x0f\n\nTYPE_16SC1\x10\xdd\x0f\x12\x0f\n\nTYPE_16SC2\x10\xde\x0f\x12\x0f\n\nTYPE_16SC3\x10\xdf\x0f\x12\x0f\n\nTYPE_16SC4\x10\xe0\x0f\x12\x0f\n\nTYPE_32SC1\x10\xe1\x0f\x12\x0f\n\nTYPE_32SC2\x10\xe2\x0f\x12\x0f\n\nTYPE_32SC3\x10\xe3\x0f\x12\x0f\n\nTYPE_32SC4\x10\xe4\x0f\x12\x0f\n\nTYPE_32FC1\x10\xe5\x0f\x12\x0f\n\nTYPE_32FC2\x10\xe6\x0f\x12\x0f\n\nTYPE_32FC3\x10\xe7\x0f\x12\x0f\n\nTYPE_32FC4\x10\xe8\x0f\x12\x0f\n\nTYPE_64FC1\x10\xe9\x0f\x12\x0f\n\nTYPE_64FC2\x10\xea\x0f\x12\x0f\n\nTYPE_64FC3\x10\xeb\x0f\x12\x0f\n\nTYPE_64FC4\x10\xec\x0f\x12\x10\n\x0b\x42\x41YER_RGGB8\x10\xb9\x17\x12\x10\n\x0b\x42\x41YER_BGGR8\x10\xba\x17\x12\x10\n\x0b\x42\x41YER_GBRG8\x10\xbb\x17\x12\x10\n\x0b\x42\x41YER_GRBG8\x10\xbc\x17\x12\x11\n\x0c\x42\x41YER_RGGB16\x10\xbd\x17\x12\x11\n\x0c\x42\x41YER_BGGR16\x10\xbe\x17\x12\x11\n\x0c\x42\x41YER_GBRG16\x10\xbf\x17\x12\x11\n\x0c\x42\x41YER_GRBG16\x10\xc0\x17\x12\x0b\n\x06YUV422\x10\xa1\x1f')
  ,
  dependencies=[modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,])

_PIXELFORMAT = _descriptor.EnumDescriptor(
  name='PixelFormat',
  full_name='apollo.drivers.PixelFormat',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RGB8', index=0, number=1001,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RGBA8', index=1, number=1002,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RGB16', index=2, number=1003,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RGBA16', index=3, number=1004,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BGR8', index=4, number=1005,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BGRA8', index=5, number=1006,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BGR16', index=6, number=1007,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BGRA16', index=7, number=1008,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MONO8', index=8, number=1009,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MONO16', index=9, number=1010,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_8UC1', index=10, number=2001,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_8UC2', index=11, number=2002,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_8UC3', index=12, number=2003,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_8UC4', index=13, number=2004,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_8SC1', index=14, number=2005,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_8SC2', index=15, number=2006,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_8SC3', index=16, number=2007,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_8SC4', index=17, number=2008,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_16UC1', index=18, number=2009,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_16UC2', index=19, number=2010,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_16UC3', index=20, number=2011,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_16UC4', index=21, number=2012,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_16SC1', index=22, number=2013,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_16SC2', index=23, number=2014,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_16SC3', index=24, number=2015,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_16SC4', index=25, number=2016,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_32SC1', index=26, number=2017,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_32SC2', index=27, number=2018,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_32SC3', index=28, number=2019,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_32SC4', index=29, number=2020,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_32FC1', index=30, number=2021,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_32FC2', index=31, number=2022,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_32FC3', index=32, number=2023,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_32FC4', index=33, number=2024,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_64FC1', index=34, number=2025,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_64FC2', index=35, number=2026,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_64FC3', index=36, number=2027,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_64FC4', index=37, number=2028,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAYER_RGGB8', index=38, number=3001,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAYER_BGGR8', index=39, number=3002,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAYER_GBRG8', index=40, number=3003,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAYER_GRBG8', index=41, number=3004,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAYER_RGGB16', index=42, number=3005,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAYER_BGGR16', index=43, number=3006,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAYER_GBRG16', index=44, number=3007,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAYER_GRBG16', index=45, number=3008,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YUV422', index=46, number=4001,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=419,
  serialized_end=1182,
)
_sym_db.RegisterEnumDescriptor(_PIXELFORMAT)

PixelFormat = enum_type_wrapper.EnumTypeWrapper(_PIXELFORMAT)
RGB8 = 1001
RGBA8 = 1002
RGB16 = 1003
RGBA16 = 1004
BGR8 = 1005
BGRA8 = 1006
BGR16 = 1007
BGRA16 = 1008
MONO8 = 1009
MONO16 = 1010
TYPE_8UC1 = 2001
TYPE_8UC2 = 2002
TYPE_8UC3 = 2003
TYPE_8UC4 = 2004
TYPE_8SC1 = 2005
TYPE_8SC2 = 2006
TYPE_8SC3 = 2007
TYPE_8SC4 = 2008
TYPE_16UC1 = 2009
TYPE_16UC2 = 2010
TYPE_16UC3 = 2011
TYPE_16UC4 = 2012
TYPE_16SC1 = 2013
TYPE_16SC2 = 2014
TYPE_16SC3 = 2015
TYPE_16SC4 = 2016
TYPE_32SC1 = 2017
TYPE_32SC2 = 2018
TYPE_32SC3 = 2019
TYPE_32SC4 = 2020
TYPE_32FC1 = 2021
TYPE_32FC2 = 2022
TYPE_32FC3 = 2023
TYPE_32FC4 = 2024
TYPE_64FC1 = 2025
TYPE_64FC2 = 2026
TYPE_64FC3 = 2027
TYPE_64FC4 = 2028
BAYER_RGGB8 = 3001
BAYER_BGGR8 = 3002
BAYER_GBRG8 = 3003
BAYER_GRBG8 = 3004
BAYER_RGGB16 = 3005
BAYER_BGGR16 = 3006
BAYER_GBRG16 = 3007
BAYER_GRBG16 = 3008
YUV422 = 4001



_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='apollo.drivers.Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.drivers.Image.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame_id', full_name='apollo.drivers.Image.frame_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='measurement_time', full_name='apollo.drivers.Image.measurement_time', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='apollo.drivers.Image.height', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='apollo.drivers.Image.width', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoding', full_name='apollo.drivers.Image.encoding', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='step', full_name='apollo.drivers.Image.step', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='apollo.drivers.Image.data', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=263,
)


_COMPRESSEDIMAGE = _descriptor.Descriptor(
  name='CompressedImage',
  full_name='apollo.drivers.CompressedImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.drivers.CompressedImage.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame_id', full_name='apollo.drivers.CompressedImage.frame_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='format', full_name='apollo.drivers.CompressedImage.format', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='apollo.drivers.CompressedImage.data', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='measurement_time', full_name='apollo.drivers.CompressedImage.measurement_time', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame_type', full_name='apollo.drivers.CompressedImage.frame_type', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=416,
)

_IMAGE.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_COMPRESSEDIMAGE.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['CompressedImage'] = _COMPRESSEDIMAGE
DESCRIPTOR.enum_types_by_name['PixelFormat'] = _PIXELFORMAT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), dict(
  DESCRIPTOR = _IMAGE,
  __module__ = 'modules.drivers.proto.sensor_image_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.Image)
  ))
_sym_db.RegisterMessage(Image)

CompressedImage = _reflection.GeneratedProtocolMessageType('CompressedImage', (_message.Message,), dict(
  DESCRIPTOR = _COMPRESSEDIMAGE,
  __module__ = 'modules.drivers.proto.sensor_image_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.CompressedImage)
  ))
_sym_db.RegisterMessage(CompressedImage)


# @@protoc_insertion_point(module_scope)
