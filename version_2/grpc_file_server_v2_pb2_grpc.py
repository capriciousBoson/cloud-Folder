# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import grpc_file_server_v2_pb2 as grpc__file__server__v2__pb2

GRPC_GENERATED_VERSION = '1.64.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in grpc_file_server_v2_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class FileServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UploadFile = channel.unary_unary(
                '/FileService/UploadFile',
                request_serializer=grpc__file__server__v2__pb2.FileUploadRequest.SerializeToString,
                response_deserializer=grpc__file__server__v2__pb2.FileUploadResponse.FromString,
                _registered_method=True)
        self.DeleteFile = channel.unary_unary(
                '/FileService/DeleteFile',
                request_serializer=grpc__file__server__v2__pb2.FileDeleteRequest.SerializeToString,
                response_deserializer=grpc__file__server__v2__pb2.FileDeleteResponse.FromString,
                _registered_method=True)


class FileServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UploadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UploadFile': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadFile,
                    request_deserializer=grpc__file__server__v2__pb2.FileUploadRequest.FromString,
                    response_serializer=grpc__file__server__v2__pb2.FileUploadResponse.SerializeToString,
            ),
            'DeleteFile': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteFile,
                    request_deserializer=grpc__file__server__v2__pb2.FileDeleteRequest.FromString,
                    response_serializer=grpc__file__server__v2__pb2.FileDeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('FileService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class FileService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UploadFile(request,
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
            '/FileService/UploadFile',
            grpc__file__server__v2__pb2.FileUploadRequest.SerializeToString,
            grpc__file__server__v2__pb2.FileUploadResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteFile(request,
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
            '/FileService/DeleteFile',
            grpc__file__server__v2__pb2.FileDeleteRequest.SerializeToString,
            grpc__file__server__v2__pb2.FileDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class DirectoryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MakeDirectory = channel.unary_unary(
                '/DirectoryService/MakeDirectory',
                request_serializer=grpc__file__server__v2__pb2.MakeDirectoryRequest.SerializeToString,
                response_deserializer=grpc__file__server__v2__pb2.MakeDirectoryResponse.FromString,
                _registered_method=True)


class DirectoryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def MakeDirectory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DirectoryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MakeDirectory': grpc.unary_unary_rpc_method_handler(
                    servicer.MakeDirectory,
                    request_deserializer=grpc__file__server__v2__pb2.MakeDirectoryRequest.FromString,
                    response_serializer=grpc__file__server__v2__pb2.MakeDirectoryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DirectoryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('DirectoryService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class DirectoryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def MakeDirectory(request,
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
            '/DirectoryService/MakeDirectory',
            grpc__file__server__v2__pb2.MakeDirectoryRequest.SerializeToString,
            grpc__file__server__v2__pb2.MakeDirectoryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)