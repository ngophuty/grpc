# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: blog_proto/post.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x62log_proto/post.proto\x12\nblog_proto\x1a\x1bgoogle/protobuf/empty.proto\"2\n\x04Post\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t2@\n\x0ePostController\x12.\n\x06\x43reate\x12\x10.blog_proto.Post\x1a\x10.blog_proto.Post\"\x00\x62\x06proto3')



_POST = DESCRIPTOR.message_types_by_name['Post']
Post = _reflection.GeneratedProtocolMessageType('Post', (_message.Message,), {
  'DESCRIPTOR' : _POST,
  '__module__' : 'blog_proto.post_pb2'
  # @@protoc_insertion_point(class_scope:blog_proto.Post)
  })
_sym_db.RegisterMessage(Post)

_POSTCONTROLLER = DESCRIPTOR.services_by_name['PostController']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _POST._serialized_start=66
  _POST._serialized_end=116
  _POSTCONTROLLER._serialized_start=118
  _POSTCONTROLLER._serialized_end=182
# @@protoc_insertion_point(module_scope)
