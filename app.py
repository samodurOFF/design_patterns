from generate_request import get_content
from views import View_Errors
import pandas as pd


class Simple_App:
    def __init__(self, routes, titles):
        self.routes = routes
        self.titles = titles

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        method = environ['REQUEST_METHOD']

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

        if method == 'POST':
            self.post_processing(environ, request)

        return body

    def post_processing(self, environ, request):
        file_name = environ['wsgi.input'].read().decode('utf-8').split('=')[1]
        if file_name:
            df = pd.DataFrame(request['table'])
            print(df)
            df.to_csv(f'{file_name}.csv', index=False, encoding='utf-8')
