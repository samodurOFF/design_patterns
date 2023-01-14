from tabulate import tabulate
from templator import render
from variables import ok_code, error_code


class View_Vars:
    def __call__(self, request):
        request['table'] = tabulate(request['table'], headers='keys', tablefmt='html')
        return ok_code, [render('index.html', **request).encode('utf-8')]


class View_Errors:
    def __call__(self, request):
        return error_code, [b'404 PAGE Not Found']


routes = {
    '/cgi_vars/': View_Vars(),
    '/all_vars/': View_Vars(),
}
