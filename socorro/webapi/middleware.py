from statsd import StatsClient
import web

statsd = StatsClient(host='localhost', port=8125, prefix='')

class Middleware(object):

    def __init__(self, wrap_app):
        self.wrap_app = wrap_app

    def __call__(self, request, response):

        response_iter = self.wrap_app(request, response)
        response_string = ''.join(response_iter)

        metric = "socorro.{0}.{1}.{2}".format(
            request['REQUEST_METHOD'],
            request['PATH_INFO'].strip('/').replace('.', '-'),
            response_string
        )
        print metric
        statsd.incr(metric)
        return [response_string]
