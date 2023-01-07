CGI_vars = ['SERVER_NAME',
            'GATEWAY_INTERFACE',
            'SERVER_PORT',
            'REMOTE_HOST',
            'CONTENT_LENGTH',
            'SCRIPT_NAME',
            'SERVER_PROTOCOL',
            'SERVER_SOFTWARE',
            'REQUEST_METHOD',
            'PATH_INFO',
            'QUERY_STRING',
            'REMOTE_ADDR',
            'CONTENT_TYPE',
            'HTTP_',
            'wsgi']

ok_code = '200 OK'
error_code = '404 error'
headers = [('Content-type', 'text/plain')]
titles = {
    '/cgi_vars/': 'CGI переменные окружения',
    '/all_vars/': 'Все переменные окружения',
}
