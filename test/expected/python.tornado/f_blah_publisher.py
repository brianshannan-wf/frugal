#
# Autogenerated by Frugal Compiler (1.24.0)
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

from .ttypes import *




class blahPublisher(object):

    _DELIMITER = '.'

    def __init__(self, provider, middleware=None):
        """
        Create a new blahPublisher.

        Args:
            provider: FScopeProvider
            middleware: ServiceMiddleware or list of ServiceMiddleware
        """

        if middleware and not isinstance(middleware, list):
            middleware = [middleware]
        self._transport, protocol_factory = provider.new()
        self._protocol = protocol_factory.get_protocol(self._transport)
        self._methods = {
            'publish_DoStuff': Method(self._publish_DoStuff, middleware),
        }

    @gen.coroutine
    def open(self):
        yield self._transport.open()

    @gen.coroutine
    def close(self):
        yield self._transport.close()

    def publish_DoStuff(self, ctx, req):
        """
        Args:
            ctx: FContext
            req: Thing
        """
        self._methods['publish_DoStuff']([ctx, req])

    def _publish_DoStuff(self, ctx, req):
        op = 'DoStuff'
        prefix = ''
        topic = '{}blah{}{}'.format(prefix, self._DELIMITER, op)
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
