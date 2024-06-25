# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crossplane/function/proto/v1beta1/run_function.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4crossplane/function/proto/v1beta1/run_function.proto\x12\x1e\x61piextensions.fn.proto.v1beta1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/duration.proto\"\xb0\x05\n\x12RunFunctionRequest\x12\x39\n\x04meta\x18\x01 \x01(\x0b\x32+.apiextensions.fn.proto.v1beta1.RequestMeta\x12\x37\n\x08observed\x18\x02 \x01(\x0b\x32%.apiextensions.fn.proto.v1beta1.State\x12\x36\n\x07\x64\x65sired\x18\x03 \x01(\x0b\x32%.apiextensions.fn.proto.v1beta1.State\x12+\n\x05input\x18\x04 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x88\x01\x01\x12-\n\x07\x63ontext\x18\x05 \x01(\x0b\x32\x17.google.protobuf.StructH\x01\x88\x01\x01\x12_\n\x0f\x65xtra_resources\x18\x06 \x03(\x0b\x32\x46.apiextensions.fn.proto.v1beta1.RunFunctionRequest.ExtraResourcesEntry\x12X\n\x0b\x63redentials\x18\x07 \x03(\x0b\x32\x43.apiextensions.fn.proto.v1beta1.RunFunctionRequest.CredentialsEntry\x1a`\n\x13\x45xtraResourcesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x38\n\x05value\x18\x02 \x01(\x0b\x32).apiextensions.fn.proto.v1beta1.Resources:\x02\x38\x01\x1a_\n\x10\x43redentialsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b\x32+.apiextensions.fn.proto.v1beta1.Credentials:\x02\x38\x01\x42\x08\n\x06_inputB\n\n\x08_context\"b\n\x0b\x43redentials\x12I\n\x0f\x63redential_data\x18\x01 \x01(\x0b\x32..apiextensions.fn.proto.v1beta1.CredentialDataH\x00\x42\x08\n\x06source\"\x85\x01\n\x0e\x43redentialData\x12\x46\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x38.apiextensions.fn.proto.v1beta1.CredentialData.DataEntry\x1a+\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"D\n\tResources\x12\x37\n\x05items\x18\x01 \x03(\x0b\x32(.apiextensions.fn.proto.v1beta1.Resource\"\xc1\x02\n\x13RunFunctionResponse\x12:\n\x04meta\x18\x01 \x01(\x0b\x32,.apiextensions.fn.proto.v1beta1.ResponseMeta\x12\x36\n\x07\x64\x65sired\x18\x02 \x01(\x0b\x32%.apiextensions.fn.proto.v1beta1.State\x12\x37\n\x07results\x18\x03 \x03(\x0b\x32&.apiextensions.fn.proto.v1beta1.Result\x12-\n\x07\x63ontext\x18\x04 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x88\x01\x01\x12\x42\n\x0crequirements\x18\x05 \x01(\x0b\x32,.apiextensions.fn.proto.v1beta1.RequirementsB\n\n\x08_context\"\x1a\n\x0bRequestMeta\x12\x0b\n\x03tag\x18\x01 \x01(\t\"\xd2\x01\n\x0cRequirements\x12Y\n\x0f\x65xtra_resources\x18\x01 \x03(\x0b\x32@.apiextensions.fn.proto.v1beta1.Requirements.ExtraResourcesEntry\x1ag\n\x13\x45xtraResourcesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12?\n\x05value\x18\x02 \x01(\x0b\x32\x30.apiextensions.fn.proto.v1beta1.ResourceSelector:\x02\x38\x01\"\x99\x01\n\x10ResourceSelector\x12\x13\n\x0b\x61pi_version\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12\x14\n\nmatch_name\x18\x03 \x01(\tH\x00\x12\x43\n\x0cmatch_labels\x18\x04 \x01(\x0b\x32+.apiextensions.fn.proto.v1beta1.MatchLabelsH\x00\x42\x07\n\x05match\"\x85\x01\n\x0bMatchLabels\x12G\n\x06labels\x18\x01 \x03(\x0b\x32\x37.apiextensions.fn.proto.v1beta1.MatchLabels.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"P\n\x0cResponseMeta\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12+\n\x03ttl\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationH\x00\x88\x01\x01\x42\x06\n\x04_ttl\"\xe9\x01\n\x05State\x12;\n\tcomposite\x18\x01 \x01(\x0b\x32(.apiextensions.fn.proto.v1beta1.Resource\x12G\n\tresources\x18\x02 \x03(\x0b\x32\x34.apiextensions.fn.proto.v1beta1.State.ResourcesEntry\x1aZ\n\x0eResourcesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32(.apiextensions.fn.proto.v1beta1.Resource:\x02\x38\x01\"\x82\x02\n\x08Resource\x12)\n\x08resource\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12[\n\x12\x63onnection_details\x18\x02 \x03(\x0b\x32?.apiextensions.fn.proto.v1beta1.Resource.ConnectionDetailsEntry\x12\x34\n\x05ready\x18\x03 \x01(\x0e\x32%.apiextensions.fn.proto.v1beta1.Ready\x1a\x38\n\x16\x43onnectionDetailsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"U\n\x06Result\x12:\n\x08severity\x18\x01 \x01(\x0e\x32(.apiextensions.fn.proto.v1beta1.Severity\x12\x0f\n\x07message\x18\x02 \x01(\t*?\n\x05Ready\x12\x15\n\x11READY_UNSPECIFIED\x10\x00\x12\x0e\n\nREADY_TRUE\x10\x01\x12\x0f\n\x0bREADY_FALSE\x10\x02*c\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x12\n\x0eSEVERITY_FATAL\x10\x01\x12\x14\n\x10SEVERITY_WARNING\x10\x02\x12\x13\n\x0fSEVERITY_NORMAL\x10\x03\x32\x91\x01\n\x15\x46unctionRunnerService\x12x\n\x0bRunFunction\x12\x32.apiextensions.fn.proto.v1beta1.RunFunctionRequest\x1a\x33.apiextensions.fn.proto.v1beta1.RunFunctionResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'crossplane.function.proto.v1beta1.run_function_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_RUNFUNCTIONREQUEST_EXTRARESOURCESENTRY']._options = None
  _globals['_RUNFUNCTIONREQUEST_EXTRARESOURCESENTRY']._serialized_options = b'8\001'
  _globals['_RUNFUNCTIONREQUEST_CREDENTIALSENTRY']._options = None
  _globals['_RUNFUNCTIONREQUEST_CREDENTIALSENTRY']._serialized_options = b'8\001'
  _globals['_CREDENTIALDATA_DATAENTRY']._options = None
  _globals['_CREDENTIALDATA_DATAENTRY']._serialized_options = b'8\001'
  _globals['_REQUIREMENTS_EXTRARESOURCESENTRY']._options = None
  _globals['_REQUIREMENTS_EXTRARESOURCESENTRY']._serialized_options = b'8\001'
  _globals['_MATCHLABELS_LABELSENTRY']._options = None
  _globals['_MATCHLABELS_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_STATE_RESOURCESENTRY']._options = None
  _globals['_STATE_RESOURCESENTRY']._serialized_options = b'8\001'
  _globals['_RESOURCE_CONNECTIONDETAILSENTRY']._options = None
  _globals['_RESOURCE_CONNECTIONDETAILSENTRY']._serialized_options = b'8\001'
  _globals['_READY']._serialized_start=2670
  _globals['_READY']._serialized_end=2733
  _globals['_SEVERITY']._serialized_start=2735
  _globals['_SEVERITY']._serialized_end=2834
  _globals['_RUNFUNCTIONREQUEST']._serialized_start=151
  _globals['_RUNFUNCTIONREQUEST']._serialized_end=839
  _globals['_RUNFUNCTIONREQUEST_EXTRARESOURCESENTRY']._serialized_start=624
  _globals['_RUNFUNCTIONREQUEST_EXTRARESOURCESENTRY']._serialized_end=720
  _globals['_RUNFUNCTIONREQUEST_CREDENTIALSENTRY']._serialized_start=722
  _globals['_RUNFUNCTIONREQUEST_CREDENTIALSENTRY']._serialized_end=817
  _globals['_CREDENTIALS']._serialized_start=841
  _globals['_CREDENTIALS']._serialized_end=939
  _globals['_CREDENTIALDATA']._serialized_start=942
  _globals['_CREDENTIALDATA']._serialized_end=1075
  _globals['_CREDENTIALDATA_DATAENTRY']._serialized_start=1032
  _globals['_CREDENTIALDATA_DATAENTRY']._serialized_end=1075
  _globals['_RESOURCES']._serialized_start=1077
  _globals['_RESOURCES']._serialized_end=1145
  _globals['_RUNFUNCTIONRESPONSE']._serialized_start=1148
  _globals['_RUNFUNCTIONRESPONSE']._serialized_end=1469
  _globals['_REQUESTMETA']._serialized_start=1471
  _globals['_REQUESTMETA']._serialized_end=1497
  _globals['_REQUIREMENTS']._serialized_start=1500
  _globals['_REQUIREMENTS']._serialized_end=1710
  _globals['_REQUIREMENTS_EXTRARESOURCESENTRY']._serialized_start=1607
  _globals['_REQUIREMENTS_EXTRARESOURCESENTRY']._serialized_end=1710
  _globals['_RESOURCESELECTOR']._serialized_start=1713
  _globals['_RESOURCESELECTOR']._serialized_end=1866
  _globals['_MATCHLABELS']._serialized_start=1869
  _globals['_MATCHLABELS']._serialized_end=2002
  _globals['_MATCHLABELS_LABELSENTRY']._serialized_start=1957
  _globals['_MATCHLABELS_LABELSENTRY']._serialized_end=2002
  _globals['_RESPONSEMETA']._serialized_start=2004
  _globals['_RESPONSEMETA']._serialized_end=2084
  _globals['_STATE']._serialized_start=2087
  _globals['_STATE']._serialized_end=2320
  _globals['_STATE_RESOURCESENTRY']._serialized_start=2230
  _globals['_STATE_RESOURCESENTRY']._serialized_end=2320
  _globals['_RESOURCE']._serialized_start=2323
  _globals['_RESOURCE']._serialized_end=2581
  _globals['_RESOURCE_CONNECTIONDETAILSENTRY']._serialized_start=2525
  _globals['_RESOURCE_CONNECTIONDETAILSENTRY']._serialized_end=2581
  _globals['_RESULT']._serialized_start=2583
  _globals['_RESULT']._serialized_end=2668
  _globals['_FUNCTIONRUNNERSERVICE']._serialized_start=2837
  _globals['_FUNCTIONRUNNERSERVICE']._serialized_end=2982
# @@protoc_insertion_point(module_scope)
