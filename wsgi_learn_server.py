# -*- coding:UTF-8 -*-

from wsgi_learn_app import application
from wsgiref.simple_server import make_server

httpd = make_server("", 8000, application)
print("servering Http at port 8000")
httpd.serve_forever()