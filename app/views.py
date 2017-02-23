import falcon
import json


def response_handler(f):
    def handler(resource, request, response, **kwargs):
        try:
            content = f(resource, request, response, **kwargs)
            response.status = falcon.HTTP_200
        except BaseException, e:
            content = dict(success=False, error=str(e))
            response.status = falcon.HTTP_500
        response.body = json.dumps(content)
    return handler


def get_query_parameters(request):
    return falcon.uri.parse_query_string(request.query_string)


class HelloView():
    @response_handler
    def on_get(self, request, response):
        return 'Hello'


class MultiplicationView():
    @response_handler
    def on_get(self, request, response):
        parameters = get_query_parameters(request)
        a = int(parameters.get('a', 0))
        b = int(parameters.get('b', 0))
        return a * b
