# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf_validation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19protobuf_validation.proto\x12\x0ekik.validation\x1a google/protobuf/descriptor.proto\"\xf4\x02\n\x0f\x46ieldValidation\x12\x18\n\tmandatory\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\r\n\x05regex\x18\x02 \x01(\t\x12\x16\n\x0emin_codepoints\x18\x03 \x01(\x05\x12\x16\n\x0emax_codepoints\x18\x04 \x01(\x05\x12\x17\n\x0fmin_byte_length\x18\x05 \x01(\x05\x12\x17\n\x0fmax_byte_length\x18\x06 \x01(\x05\x12\x0f\n\x07min_val\x18\x07 \x01(\x10\x12\x0f\n\x07max_val\x18\x08 \x01(\x10\x12\x16\n\x0emin_double_val\x18\x0b \x01(\x01\x12\x16\n\x0emax_double_val\x18\x0c \x01(\x01\x12\x17\n\x0fmin_repetitions\x18\x0f \x01(\r\x12\x17\n\x0fmax_repetitions\x18\x10 \x01(\r\x12\x36\n\x07ordered\x18\x11 \x01(\x0e\x32%.kik.validation.FieldValidation.Order\"\x1a\n\x05Order\x12\x07\n\x03\x41SC\x10\x00\x12\x08\n\x04\x44\x45SC\x10\x01:Z\n\x10\x66ield_validation\x12\x1d.google.protobuf.FieldOptions\x18\xd9\xd3\x04 \x01(\x0b\x32\x1f.kik.validation.FieldValidation:Q\n\x07map_key\x12\x1d.google.protobuf.FieldOptions\x18\xda\xd3\x04 \x01(\x0b\x32\x1f.kik.validation.FieldValidationBl\n\x17\x63om.kik.protovalidationZQgithub.com/kikinteractive/xiphias-model-common/generated/go/kikoptions;kikoptions')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protobuf_validation_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(field_validation)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(map_key)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.kik.protovalidationZQgithub.com/kikinteractive/xiphias-model-common/generated/go/kikoptions;kikoptions'
  _FIELDVALIDATION._serialized_start=80
  _FIELDVALIDATION._serialized_end=452
  _FIELDVALIDATION_ORDER._serialized_start=426
  _FIELDVALIDATION_ORDER._serialized_end=452
# @@protoc_insertion_point(module_scope)
