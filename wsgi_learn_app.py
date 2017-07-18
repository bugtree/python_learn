# -*- coding:UTF-8 -*-

def application(env, response):
    response("200 OK", [("content-type", "text/html")])
    body = "<h1>hello, %s</h1>" % env["PATH_INFO"][1:] or "web"
    return [body.encode("utf-8")]