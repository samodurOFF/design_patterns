from wsgiref.simple_server import make_server
from app import Simple_App
from variables import titles
from views import routes

application = Simple_App(routes, titles)

with make_server('', 8000, application) as httpd:
    print("Serving on http://localhost:8000/")
    httpd.serve_forever()
