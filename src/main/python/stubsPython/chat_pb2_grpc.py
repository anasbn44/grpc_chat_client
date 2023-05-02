# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import chat_pb2 as chat__pb2


class ChatServicesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.connexion = channel.stream_stream(
                '/ChatServices/connexion',
                request_serializer=chat__pb2.Client.SerializeToString,
                response_deserializer=chat__pb2.Response.FromString,
                )
        self.disconnect = channel.stream_stream(
                '/ChatServices/disconnect',
                request_serializer=chat__pb2.Client.SerializeToString,
                response_deserializer=chat__pb2.Response.FromString,
                )
        self.join = channel.stream_stream(
                '/ChatServices/join',
                request_serializer=chat__pb2.Channel.SerializeToString,
                response_deserializer=chat__pb2.Response.FromString,
                )
        self.listClient = channel.stream_stream(
                '/ChatServices/listClient',
                request_serializer=chat__pb2.Channel.SerializeToString,
                response_deserializer=chat__pb2.Response.FromString,
                )
        self.leave = channel.stream_stream(
                '/ChatServices/leave',
                request_serializer=chat__pb2.Channel.SerializeToString,
                response_deserializer=chat__pb2.Response.FromString,
                )
        self.sendMessage = channel.stream_stream(
                '/ChatServices/sendMessage',
                request_serializer=chat__pb2.Message.SerializeToString,
                response_deserializer=chat__pb2.Response.FromString,
                )


class ChatServicesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def connexion(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def disconnect(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def join(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listClient(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def leave(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendMessage(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChatServicesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'connexion': grpc.stream_stream_rpc_method_handler(
                    servicer.connexion,
                    request_deserializer=chat__pb2.Client.FromString,
                    response_serializer=chat__pb2.Response.SerializeToString,
            ),
            'disconnect': grpc.stream_stream_rpc_method_handler(
                    servicer.disconnect,
                    request_deserializer=chat__pb2.Client.FromString,
                    response_serializer=chat__pb2.Response.SerializeToString,
            ),
            'join': grpc.stream_stream_rpc_method_handler(
                    servicer.join,
                    request_deserializer=chat__pb2.Channel.FromString,
                    response_serializer=chat__pb2.Response.SerializeToString,
            ),
            'listClient': grpc.stream_stream_rpc_method_handler(
                    servicer.listClient,
                    request_deserializer=chat__pb2.Channel.FromString,
                    response_serializer=chat__pb2.Response.SerializeToString,
            ),
            'leave': grpc.stream_stream_rpc_method_handler(
                    servicer.leave,
                    request_deserializer=chat__pb2.Channel.FromString,
                    response_serializer=chat__pb2.Response.SerializeToString,
            ),
            'sendMessage': grpc.stream_stream_rpc_method_handler(
                    servicer.sendMessage,
                    request_deserializer=chat__pb2.Message.FromString,
                    response_serializer=chat__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ChatServices', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ChatServices(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def connexion(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/ChatServices/connexion',
            chat__pb2.Client.SerializeToString,
            chat__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def disconnect(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/ChatServices/disconnect',
            chat__pb2.Client.SerializeToString,
            chat__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def join(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/ChatServices/join',
            chat__pb2.Channel.SerializeToString,
            chat__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listClient(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/ChatServices/listClient',
            chat__pb2.Channel.SerializeToString,
            chat__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def leave(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/ChatServices/leave',
            chat__pb2.Channel.SerializeToString,
            chat__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sendMessage(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/ChatServices/sendMessage',
            chat__pb2.Message.SerializeToString,
            chat__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
