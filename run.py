from wsgiref.simple_server import make_server
from simba_framework.main import Simple_App
from urls import routes, fronts

application = Simple_App(routes, fronts)

with make_server('', 8000, application) as httpd:
    print("Serving on http://localhost:8000/")
    httpd.serve_forever()
