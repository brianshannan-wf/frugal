#
# Autogenerated by Frugal Compiler (1.14.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#



import sys
import traceback

from thrift.Thrift import TApplicationException
from thrift.Thrift import TMessageType
from thrift.Thrift import TType
from tornado import gen
from frugal.middleware import Method
from frugal.subscription import FSubscription

from v1.music.ttypes import *




class AlbumWinnersPublisher(object):
    """
    Scopes are a Frugal extension to the IDL for declaring PubSub
    semantics. Subscribers to this scope will be notified if they win a contest.
    Scopes must have a prefix.
    """

    _DELIMITER = '.'

    def __init__(self, provider, middleware=None):
        """
        Create a new AlbumWinnersPublisher.

        Args:
            provider: FScopeProvider
            middleware: ServiceMiddleware or list of ServiceMiddleware
        """

        if middleware and not isinstance(middleware, list):
            middleware = [middleware]
        self._transport, protocol_factory = provider.new()
        self._protocol = protocol_factory.get_protocol(self._transport)
        self._methods = {
            'publish_Winner': Method(self._publish_Winner, middleware),
        }

    @gen.coroutine
    def open(self):
        yield self._transport.open()

    @gen.coroutine
    def close(self):
        yield self._transport.close()

    def publish_Winner(self, ctx, req):
        """
        Args:
            ctx: FContext
            req: Album
        """
        self._methods['publish_Winner']([ctx, req])

    def _publish_Winner(self, ctx, req):
        op = 'Winner'
        prefix = 'v1.music.'
        topic = '{}AlbumWinners{}{}'.format(prefix, self._DELIMITER, op)
        oprot = self._protocol
        self._transport.lock_topic(topic)
        try:
            oprot.write_request_headers(ctx)
            oprot.writeMessageBegin(op, TMessageType.CALL, 0)
            req.write(oprot)
            oprot.writeMessageEnd()
            oprot.get_transport().flush()
        finally:
            self._transport.unlock_topic()

