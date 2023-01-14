from variables import CGI_vars


def get_content(title, request, environ):
    request['user'] = environ['USERNAME']
    request['title'] = title
    response = []
    if title == 'CGI переменные окружения':
        for key, value in environ.items():
            for cgi in CGI_vars:
                if cgi in key:
                    response.append({'Переменная': str(key), 'Значение': str(value)})

    elif title == 'Все переменные окружения':
        for key, value in environ.items():
            response.append({'Переменная': str(key), 'Значение': str(value)})

    request['table'] = response if response else None
