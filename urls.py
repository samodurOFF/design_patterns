from tabulate import tabulate
from variables import CGI_KEYS, ALL_VARS, CGI_URL, TITLES
from views import View_Vars


# front controller
def master_front(request, environ):
    request['user'] = environ['USERNAME']
    path = environ['PATH_INFO']
    print(path)
    response = []
    if path == CGI_URL:
        for key, value in environ.items():
            for cgi in CGI_KEYS:
                if cgi in key:
                    response.append({'Переменная': str(key), 'Значение': str(value)})

    elif path == ALL_VARS:
        for key, value in environ.items():
            response.append({'Переменная': str(key), 'Значение': str(value)})


    request['title'] = TITLES[path]
    request['table'] = tabulate(response, headers='keys', tablefmt='html')


fronts = [master_front]

routes = {
    CGI_URL: View_Vars(),
    ALL_VARS: View_Vars(),
}
