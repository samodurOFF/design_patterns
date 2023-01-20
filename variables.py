CGI_KEYS = ['SERVER_NAME',
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

OK = '200 OK'
CGI_URL = '/cgi_vars/'
ALL_VARS = '/all_vars/'
TITLES = {
    CGI_URL: 'CGI переменные',
    ALL_VARS: 'Все переменные'
}
ERROR = '404 error'
HEADERS = [('Content-type', 'text/plain')]
