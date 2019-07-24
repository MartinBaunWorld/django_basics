from logging import StreamHandler

from ipware import get_client_ip


class EnhancedStreamHandler(StreamHandler, object):
    def emit(self, record):
        record.ip = ''
        record.email = ''

        try:
            request = record.args[0]
            record.ip, _ = get_client_ip(request)
            record.args = None
            record.email = request.user.email
        except: # noqa
            pass
        super(EnhancedStreamHandler, self).emit(record)
