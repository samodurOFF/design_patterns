from generate_request import get_content
from views import View_Errors


class Simple_App:
    def __init__(self, routes, titles):
        self.routes = routes
        self.titles = titles

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        if path[-1] != '/':
            path += '/'

        # page controller
        if path in self.routes:
            view = self.routes[path]
            title = self.titles[path]
        else:
            view = View_Errors()
            title = 'Error'

        # front controller
        request = {}
        get_content(title, request, environ)
        code, body = view(request)

        start_response(code, [('Content-Type', 'text/html')])

        return body
