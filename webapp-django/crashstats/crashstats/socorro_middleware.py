from django_statsd.clients import statsd


class SocorroMiddleware(object):
    """
    Middleware that counts how often each url is requested
    """

    def process_response(self, method, path, status_code):
        metric = "socorro.{0}.{1}.{2}".format(
            method,
            path.strip('/').replace('.', '-'),
            status_code
        )
        print metric
        statsd.incr(metric)
