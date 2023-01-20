from simba_framework.templator import render
from variables import ERROR, OK


class View_Vars:
    def __call__(self, request):
        return OK, render('index.html', **request)


class View_Errors:
    def __call__(self, request):
        return ERROR, '404 PAGE Not Found'
