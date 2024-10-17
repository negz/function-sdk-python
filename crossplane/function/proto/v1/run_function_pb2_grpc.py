# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from crossplane.function.proto.v1 import run_function_pb2 as crossplane_dot_function_dot_proto_dot_v1_dot_run__function__pb2

GRPC_GENERATED_VERSION = '1.66.2'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in crossplane/function/proto/v1/run_function_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class FunctionRunnerServiceStub(object):
    """A FunctionRunnerService is a Composition Function.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RunFunction = channel.unary_unary(
                '/apiextensions.fn.proto.v1.FunctionRunnerService/RunFunction',
                request_serializer=crossplane_dot_function_dot_proto_dot_v1_dot_run__function__pb2.RunFunctionRequest.SerializeToString,
                response_deserializer=crossplane_dot_function_dot_proto_dot_v1_dot_run__function__pb2.RunFunctionResponse.FromString,
                _registered_method=True)


class FunctionRunnerServiceServicer(object):
    """A FunctionRunnerService is a Composition Function.
    """

    def RunFunction(self, request, context):
        """RunFunction runs the Composition Function.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FunctionRunnerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RunFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.RunFunction,
                    request_deserializer=crossplane_dot_function_dot_proto_dot_v1_dot_run__function__pb2.RunFunctionRequest.FromString,
                    response_serializer=crossplane_dot_function_dot_proto_dot_v1_dot_run__function__pb2.RunFunctionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'apiextensions.fn.proto.v1.FunctionRunnerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('apiextensions.fn.proto.v1.FunctionRunnerService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class FunctionRunnerService(object):
    """A FunctionRunnerService is a Composition Function.
    """

    @staticmethod
    def RunFunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/apiextensions.fn.proto.v1.FunctionRunnerService/RunFunction',
            crossplane_dot_function_dot_proto_dot_v1_dot_run__function__pb2.RunFunctionRequest.SerializeToString,
            crossplane_dot_function_dot_proto_dot_v1_dot_run__function__pb2.RunFunctionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
